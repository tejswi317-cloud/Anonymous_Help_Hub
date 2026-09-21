from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    abort
)

from config import Config

from anonymous import generate_anonymous_name

from database import (
    initialize_database,
    add_question,
    get_open_questions,
    get_question,
    get_user_matches,
    get_match,
    add_message,
    get_messages
)

from matching import match_helper


app = Flask(__name__)

app.config.from_object(Config)


# Initialize database when application starts.
initialize_database()


@app.before_request
def ensure_anonymous_identity():
    """
    Make sure every visitor has an anonymous identity.
    """

    if "anonymous_id" not in session:
        session["anonymous_id"] = generate_anonymous_name()


@app.route("/")
def home():

    questions = get_open_questions()

    matches = get_user_matches(
        session["anonymous_id"]
    )

    return render_template(
        "index.html",
        anonymous_id=session["anonymous_id"],
        questions=questions,
        matches=matches
    )


@app.route("/ask", methods=["GET", "POST"])
def ask():

    if request.method == "POST":

        category = request.form.get(
            "category",
            ""
        ).strip()

        title = request.form.get(
            "title",
            ""
        ).strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        if not category or not title or not description:
            return render_template(
                "ask.html",
                error="Please fill in all fields."
            )

        if len(title) > 150:
            return render_template(
                "ask.html",
                error="Title is too long."
            )

        if len(description) > Config.MAX_QUESTION_LENGTH:
            return render_template(
                "ask.html",
                error="Description is too long."
            )

        add_question(
            session["anonymous_id"],
            category,
            title,
            description
        )

        return redirect(url_for("home"))

    return render_template("ask.html")


@app.route("/questions")
def questions():

    all_questions = get_open_questions()

    return render_template(
        "questions.html",
        questions=all_questions
    )


@app.route("/help/<int:question_id>")
def help_question(question_id):

    helper_id = session["anonymous_id"]

    match_id = match_helper(
        question_id,
        helper_id
    )

    if match_id is None:
        return render_template(
            "error.html",
            message=(
                "This question is no longer available "
                "or you cannot help your own question."
            )
        )

    return redirect(
        url_for(
            "chat",
            match_id=match_id
        )
    )


@app.route("/chat/<int:match_id>", methods=["GET", "POST"])
def chat(match_id):

    match = get_match(match_id)

    if match is None:
        abort(404)

    current_user = session["anonymous_id"]

    # Security check:
    # only participants can access the chat.
    if (
        current_user != match["asker_id"]
        and current_user != match["helper_id"]
    ):
        abort(403)

    if request.method == "POST":

        message = request.form.get(
            "message",
            ""
        ).strip()

        if message:

            if len(message) > Config.MAX_MESSAGE_LENGTH:
                return render_template(
                    "chat.html",
                    match=match,
                    messages=get_messages(match_id),
                    error="Message is too long."
                )

            add_message(
                match_id,
                current_user,
                message
            )

        return redirect(
            url_for(
                "chat",
                match_id=match_id
            )
        )

    messages = get_messages(match_id)

    return render_template(
        "chat.html",
        match=match,
        messages=messages
    )


@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "error.html",
        message="The requested page was not found."
    ), 404


@app.errorhandler(403)
def access_denied(error):

    return render_template(
        "error.html",
        message="You do not have permission to access this page."
    ), 403


if __name__ == "__main__":
    app.run(
        debug=True
    )