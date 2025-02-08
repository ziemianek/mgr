from uuid import uuid4


def generate_uuid():
    """
     Generates a random UUID (Universally Unique Identifier).

    Returns:
        str: A string representation of a randomly generated UUID.
    """
    return str(uuid4())
