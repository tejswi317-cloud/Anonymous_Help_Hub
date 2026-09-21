import sqlite3
from config import Config


def get_connection():
    """
    Create a connection to the SQLite database.
    """

    connection = sqlite3.connect(Config.DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create all required database tables.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            anonymous_id TEXT NOT NULL,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            asker_id TEXT NOT NULL,
            helper_id TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(question_id) REFERENCES questions(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER NOT NULL,
            sender_id TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(match_id) REFERENCES matches(id)
        )
    """)

    connection.commit()

    connection.close()


def add_question(anonymous_id, category, title, description):
    """
    Add a new help request.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO questions
        (anonymous_id, category, title, description)
        VALUES (?, ?, ?, ?)
    """, (
        anonymous_id,
        category,
        title,
        description
    ))

    question_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return question_id


def get_open_questions():
    """
    Return all questions that are currently open.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM questions
        WHERE status = 'open'
        ORDER BY created_at DESC
    """)

    questions = cursor.fetchall()

    connection.close()

    return questions


def get_question(question_id):
    """
    Find a question using its ID.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM questions
        WHERE id = ?
    """, (question_id,))

    question = cursor.fetchone()

    connection.close()

    return question


def update_question_status(question_id, status):
    """
    Change question status.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE questions
        SET status = ?
        WHERE id = ?
    """, (status, question_id))

    connection.commit()

    connection.close()


def create_match(question_id, asker_id, helper_id):
    """
    Create a match between an asker and a helper.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO matches
        (question_id, asker_id, helper_id)
        VALUES (?, ?, ?)
    """, (
        question_id,
        asker_id,
        helper_id
    ))

    match_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return match_id


def get_match(match_id):
    """
    Get match information.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM matches
        WHERE id = ?
    """, (match_id,))

    match = cursor.fetchone()

    connection.close()

    return match


def get_user_matches(anonymous_id):
    """
    Return matches belonging to the current anonymous user.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM matches
        WHERE asker_id = ?
           OR helper_id = ?
        ORDER BY created_at DESC
    """, (
        anonymous_id,
        anonymous_id
    ))

    matches = cursor.fetchall()

    connection.close()

    return matches


def add_message(match_id, sender_id, message):
    """
    Store an anonymous chat message.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO messages
        (match_id, sender_id, message)
        VALUES (?, ?, ?)
    """, (
        match_id,
        sender_id,
        message
    ))

    connection.commit()

    connection.close()


def get_messages(match_id):
    """
    Return all messages belonging to a match.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        WHERE match_id = ?
        ORDER BY created_at ASC
    """, (match_id,))

    messages = cursor.fetchall()

    connection.close()

    return messages