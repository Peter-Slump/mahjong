from __future__ import absolute_import

from mahjong import models

import mahjong.services.dice
import mahjong.services.stone


def create():
    """
    Initializes a new :py:class:`mahjong.models.Table`.

    :rtype: models.Table
    """
    return models.Table(stones=mahjong.services.stone.get_all_shuffled())


def open_wall(game):
    """
    Before each round the wall have to be opened. 3 dices will be rolled and the
    total of the dices determines which wall will be opened first. Starting from
    the dealers wall the walls will be counted counter clock-wise until the
    number of eyes on the dices is reached.

    From the same dice result the position in the opened wall will be
    determined by counting the stones from right to left. From that position
    the stones will be picked.



    :param :py:class:`mahjong.models.Game` game: The game to open the wall for.
    :rtype tuple:
    :return: :py:class:`mahjong.models.Game`, tuple( *dices )
    """
    table = game.table
    dices = mahjong.services.dice.roll(number_dice=3)

    assert table.position_in_wall is None, 'Wall is already opened'

    table = _select_wall_to_open(table=game.table,
                                 dealer_wind=game.prevailing_wind,
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

    return table, dices


def get_stones(table, nr_stones):
    """
    Get one or more stones from the wall.

    :type table: models.Table
    :param int nr_stones:
    :rtype: tuple
    """
    return tuple(table.stone_stack.pop() for _ in range(0, nr_stones))


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
