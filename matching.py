from database import (
    get_question,
    create_match,
    update_question_status
)


def match_helper(question_id, helper_id):
    """
    Match a helper with an open question.

    Returns:
        match ID if successful
        None if matching fails
    """

    question = get_question(question_id)

    if question is None:
        return None

    if question["status"] != "open":
        return None

    asker_id = question["anonymous_id"]

    # Prevent users from helping their own question.
    if asker_id == helper_id:
        return None

    match_id = create_match(
        question_id,
        asker_id,
        helper_id
    )

    update_question_status(
        question_id,
        "matched"
    )

    return match_id