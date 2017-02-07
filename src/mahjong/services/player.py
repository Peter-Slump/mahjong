from __future__ import absolute_import


def reset(player):
    """
    Reset the player.

    Empty hand and table
    :type player: mahjong.models.Player
    :rtype: models.Player
    """
    player.hand = None
    return player
