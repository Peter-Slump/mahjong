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
        models.WIND_SOUTH: shuffled_stones[36:72],
        models.WIND_WEST: shuffled_stones[72:108],
        models.WIND_NORTH: shuffled_stones[108:144]
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


def open_wall(table, dealer_wind, dices):
    """
    Find the place to open the wall

    :type table: models.Table
    :param tuple dices:
    :rtype: models.Table
    """
    assert table.position_in_wall is None, 'Wall is already opened'
    assert len(dices) is 3, 'Give three dices'

    table = _select_wall_to_open(table=table,
                                 dealer_wind=dealer_wind,
                                 dices=dices)

    dice_total = sum(dices)

    dice_total *= 2  # Stacks are two high

    wall_length = len(table.walls[table.current_wall])
    open_index = wall_length - dice_total - 1
    table.position_in_wall = open_index

    stone_stack = table.walls[table.current_wall][0:open_index]
    for _ in range(0, len(models.ALL_WINDS) - 1):
        _shift_open_wall(table)
        stone_stack = table.walls[table.current_wall] + stone_stack

    _shift_open_wall(table=table)
    stone_stack = table.walls[table.current_wall][open_index:] + stone_stack

    table.stone_stack = stone_stack

    return table


def _define_death_wall(table):
    """
    Pick the first 8 sets of stones and set it as death wall.
    :type table: models.Table
    :rtype: models.Table
    """
    assert table.stone_stack is not None, 'Open the wall first'

    table.death_wall = table.stone_stack[0:8]
    table.stone_stack = table.stone_stack[8:]

    return table


def _shift_open_wall(table):
    """
    Shift the open wall counter clock wise
    :type table: models.Table
    :rtype: models.Table
    """
    assert table.current_wall is not None, 'Please select wall to open first'

    wall_index = models.ALL_WINDS.index(table.current_wall)

    if wall_index == 0:
        wall_index = len(models.ALL_WINDS) - 1
    else:
        wall_index -= 1

    table.current_wall = models.ALL_WINDS[wall_index]

    return table


def _select_wall_to_open(table, dealer_wind, dices):
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

    nr_winds = len(models.ALL_WINDS)
    total_of_dices = sum(dices)
    open_wall_ = total_of_dices % nr_winds

    dealer_wind_index = models.ALL_WINDS.index(dealer_wind)
    wind_index = dealer_wind_index + open_wall_

    if wind_index > nr_winds:
        wind_index %= nr_winds

    table.current_wall = models.ALL_WINDS[wind_index - 1]

    return table


def get_stones(table, nr_stones):
    """
    Get one or more stones from the wall.

    :type table: models.Table
    :param int nr_stones:
    :rtype: tuple
    """
    return tuple(table.stone_stack.pop() for _ in range(0, nr_stones))
