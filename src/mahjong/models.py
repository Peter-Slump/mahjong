WIND_EAST = 'east'
WIND_NORTH = 'north'
WIND_WEST = 'west'
WIND_SOUTH = 'south'

ALL_WINDS = (
    WIND_EAST,
    WIND_SOUTH,
    WIND_WEST,
    WIND_NORTH,
)


class Game(object):

    players = None
    current_dealer = None
    prevailing_wind = None
    table = None

    def __init__(self, players):
        assert len(players) == 4, 'Please supply 4 players'
        for player in players:
            assert isinstance(player, Player)

        self.players = players

    def __repr__(self):
        return 'Mahjong game with: {}'.format(', '.join(map(str, self.players)))


class Player(object):
    """
    Represents a player in the game.

    :param str name: Name of the player
    """

    name = None
    hand = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Table(object):

    walls = None
    current_wall = None
    position_in_wall = None
    death_wall = None
    stone_stack = None
