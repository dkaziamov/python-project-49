from random import randint


def generate_random_number(DIFFICULTY_LEVEL: int) -> int:
    """
    Generates a random number between 1 and the given DIFFICULTY_LEVEL.

    Args:
        DIFFICULTY_LEVEL(int): The upper limit for the random number generation

    Returns:
        int: A randomly generated number between 1 and DIFFICULTY_LEVEL.
    """
    return randint(1, DIFFICULTY_LEVEL)




