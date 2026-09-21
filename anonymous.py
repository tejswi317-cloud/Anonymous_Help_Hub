import random


ADJECTIVES = [
    "Quiet",
    "Kind",
    "Brave",
    "Calm",
    "Helpful",
    "Gentle",
    "Curious",
    "Friendly",
    "Hopeful",
    "Patient"
]

NOUNS = [
    "Sparrow",
    "Cloud",
    "River",
    "Star",
    "Mountain",
    "Leaf",
    "Moon",
    "Phoenix",
    "Comet",
    "Tree"
]


def generate_anonymous_name():
    """
    Generate a random anonymous identity.

    Example:
        Quiet Sparrow 421
    """

    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    number = random.randint(100, 999)

    return f"{adjective} {noun} {number}"