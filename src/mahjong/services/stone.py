from __future__ import absolute_import

from random import shuffle

from mahjong import stones


def get_all_shuffled():
    """
    Get all stones required for Hong Kong Mahjong shuffled.

    :rtype: list
    """
    all_stones = []
    for stone_, number in stones.STONE_NUMBERS.items():
        all_stones += number * [stone_]

    shuffle(all_stones)

    return all_stones
