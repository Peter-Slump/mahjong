from mahjong import models


def reset(player):
    """
    Reset the player.

    Empty hand and table
    :type player: models.Player
    :rtype: models.Player
    """
    player.hand = None
    return player
