import random

from mahjong import models

import mahjong.services.player
import mahjong.services.table


def create(players):
    """
    Create a new game

    :param list players: List of 4 players
    :return: The created game
    :rtype: models.Game
    """
    assert len(players) == 4, 'Please supply 4 players'

    for player in players:
        assert isinstance(player, models.Player), \
            'Players should be of type Player'

    return models.Game(players=players)


def choose_first_dealer(game):
    """
    Choose the first dealer.

    One of the players is selected randomly as dealer.

    :type game: models.Game
    :rtype: models.Game
    """
    assert game.current_dealer is None, 'Dealer already set'
    assert game.players is not None, 'Please set players first'

    game.current_dealer = random.choice(game.players)

    return game


def start(game):
    """
    Start the game

    :param game: Game to start
    :type game: mahjong.models.Game
    :return: Started game
    :rtype: mahjong.models.Game
    """
    assert game.prevailing_wind is None, 'Game already started'

    choose_first_dealer(game)
    # game always start with the south wind
    game.prevailing_wind = models.WIND_EAST

    for player in game.players:
        mahjong.services.player.reset(player=player)

    game.table = mahjong.services.table.create()

    return game


def get_dice_result(nr_dices=1):
    """
    Get dice result
    :param int nr_dices: Nr. of dices to get a result from
    :return: tuple
    """
    return tuple(random.randint(1, 6) for _ in range(0, nr_dices))
