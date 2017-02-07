from __future__ import absolute_import

from random import shuffle

from mahjong.stones import STONE_NUMBERS


def get_all_shuffled():
    """
    Get all stones required for Hong Kong Mahjong shuffled.

    :rtype: list
    """
    all_stones = []
    for stone, number in STONE_NUMBERS.items():
        all_stones += number * [stone]

    shuffle(all_stones)

    return all_stones
