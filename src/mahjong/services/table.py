from __future__ import absolute_import

from mahjong.models import ALL_WINDS, Table

import mahjong.services.dice
import mahjong.services.stone


def create():
    """
    Initializes a new :py:class:`mahjong.models.Table`.

    :rtype: Table
    """
    return Table(stones=mahjong.services.stone.get_all_shuffled())


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
    :return: :py:class:`mahjong.models.Game`, tuple( *dice )
    """
    table = game.table
    dice = mahjong.services.dice.roll(number_dice=3)

    assert table.wall_index is None, 'Wall is already opened'

    table = _select_wall_to_open(table=table,
                                 dealer_wind=game.prevailing_wind,
                                 dices=dice)

    table.wall_index = _select_stone_in_wall(table=table, dice=dice)

    return table, dice


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


def _select_wall_to_open(table, dealer_wind, dices):
    """
    Select wall to open.

    :type table: models.Table
    :param str dealer_wind: The wind of the current dealer
    :param tuple dices: two or three dices to sum
    :rtype: models.Table
    """
    assert table.wall_wind is None, 'Wall to open already selected'
    assert dealer_wind in table.walls.keys(), \
        'Dealer wind should be one of the wall winds.'

    nr_winds = len(ALL_WINDS)
    total_of_dices = sum(dices)
    open_wall_ = total_of_dices % nr_winds

    dealer_wind_index = ALL_WINDS.index(dealer_wind)
    wind_index = dealer_wind_index + open_wall_

    if wind_index > nr_winds:
        wind_index %= nr_winds

    table.wall_wind = ALL_WINDS[wind_index - 1]

    return table


def _select_stone_in_wall(table, dice):
    """
    Get the index where the wall should be opened.

    :param :py:class:`mahjong.models.Table' table:
    :param tuple dice:
    :return: int
    """
    dice_total = sum(dice)
    dice_total *= 2  # Stacks are two high

    wall = table.walls[table.wall_wind]
    wall_length = len(wall)
    open_index = wall_length - dice_total - 1
    return open_index
