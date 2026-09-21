from dataclasses import dataclass


@dataclass
class Question:
    id: int
    anonymous_id: str
    category: str
    title: str
    description: str
    status: str


@dataclass
class Match:
    id: int
    question_id: int
    asker_id: str
    helper_id: str
    status: str


@dataclass
class Message:
    id: int
    match_id: int
    sender_id: str
    message: str