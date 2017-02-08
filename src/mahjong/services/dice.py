import random


def roll(number_dice=1):
    """
    Get dice result

    :param int number_dice: Nr. of dice to get a result from
    :return: tuple with the same length as requested number of dice.
    """
    return tuple(random.randint(1, 6) for _ in range(0, number_dice))
