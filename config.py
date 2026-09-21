import os


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "anonymous-help-hub-development-key"
    )

    DATABASE = os.environ.get(
        "DATABASE",
        "help_hub.db"
    )

    MAX_QUESTION_LENGTH = 1000
    MAX_MESSAGE_LENGTH = 500