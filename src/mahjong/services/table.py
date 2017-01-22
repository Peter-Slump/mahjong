from random import shuffle

from mahjong import models
from mahjong import stones


def create():
    """
    Create new table

    :rtype: models.Table
    """

    table = models.Table()

    shuffled_stones = get_shuffled_stones()
    table.walls = {
        models.WIND_EAST: shuffled_stones[0:36],
        models.WIND_SOUTH: shuffled_stones[35:71],
        models.WIND_WEST: shuffled_stones[71:107],
        models.WIND_NORTH: shuffled_stones[106:142]
    }

    return table


def get_shuffled_stones():
    """
    Get a set of shuffled stones

    :rtype: list
    """
    all_stones = []
    for stone, number in stones.STONE_NUMBERS.items():
        all_stones += number * [stone]

    shuffle(all_stones)

    return all_stones


def select_wall_to_open(table, dealer_wind, dices):
    """
    Select wall to open.

    :type table: models.Table
    :param str dealer_wind: The wind of the current dealer
    :param tuple dices: two or three dices to sum
    :rtype: models.Table
    """
    assert table.current_wall is None, 'Wall to open already selected'
    assert dealer_wind in table.walls.keys(), \
        'Dealer wind should be one of the wall winds.'
    assert len(dices) in (2, 3), 'Give two or three dices'

    nr_winds = len(models.ALL_WINDS)
    total_of_dices = sum(dices)
    open_wall = total_of_dices % nr_winds

    dealer_wind_index = models.ALL_WINDS.index(dealer_wind)
    wind_index = dealer_wind_index + open_wall

    if wind_index > nr_winds:
        wind_index = wind_index % nr_winds

    table.current_wall = models.ALL_WINDS[wind_index - 1]

    return table
