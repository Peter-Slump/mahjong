from __future__ import absolute_import

import random

from mahjong.models import Game, Player, WIND_EAST

import mahjong.services.player
import mahjong.services.table


def create(players):
    """
    To create a game instantiate four models of the type
    :py:class:`mahjong.models.Player` and call the service.

    >>> from mahjong.models import Player
    >>> import mahjong.services.game
    >>> players = [
    ...     Player(name='John Doe'),
    ...     Player(name='Jane'),
    ...     Player(name='Peter'),
    ...     Player(name='Josh')
    ... ]
    >>> mahjong.services.game.create(players=players)
    Mahjong game with: John Doe, Jane, Peter, Josh

    The position of the players in the list also determines the table position
    for the player.

    :param list players: List of 4 players
    :return: The created game
    :rtype: :py:class:`mahjong.models.Game`
    """
    assert len(players) == 4, 'Please supply 4 players'

    for player in players:
        assert isinstance(player, Player), \
            'Players should be of type Player'

    return Game(players=players)


def start(game):
    """
    Starting the game will set the prevailing wind to east, determines the
    current dealer (if not already determined) and creates a new
    :py:class:`mahjong.models.Table`.

    >>> from mahjong import models
    >>> import mahjong.services.game
    >>> players = [
    ...     models.Player(name='John Doe'),
    ...     models.Player(name='Jane'),
    ...     models.Player(name='Peter'),
    ...     models.Player(name='Josh')
    ... ]
    >>> game = mahjong.services.game.create(players=players)
    >>> game = mahjong.services.game.start(game=game)
    >>> game.prevailing_wind
    'east'

    :param game: Game to start
    :type game: mahjong.models.Game
    :return: Started game
    :rtype: mahjong.models.Game
    """
    assert game.prevailing_wind is None, 'Game already started'

    if game.current_dealer is None:
        choose_first_dealer(game)
    # game always start with the south wind
    game.prevailing_wind = WIND_EAST

    for player in game.players:
        mahjong.services.player.reset(player=player)

    game.table = mahjong.services.table.create()

    return game


def choose_first_dealer(game):
    """
    Determine the first dealer (optional).

    This service is optional, if not called it will be called within
    :py:func:`mahjong.services.game.start`.

    One of the players will be selected randomly as dealer.

    >>> from mahjong import models
    >>> import mahjong.services.game
    >>> players = [
    ...     models.Player(name='John Doe'),
    ...     models.Player(name='Jane'),
    ...     models.Player(name='Peter'),
    ...     models.Player(name='Josh')
    ... ]
    >>> game = mahjong.services.game.create(players=players)
    >>> game = mahjong.services.game.choose_first_dealer(game=game)
    >>> game.current_dealer  # doctest: +SKIP
    Jane

    :type game: :py:class:`mahjong.models.Game`
    :rtype: :py:class:`mahjong.models.Game`
    """
    assert game.current_dealer is None, 'Dealer already set'
    assert game.players is not None, 'Please set players first'

    game.current_dealer = random.choice(game.players)

    return game
