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

        self._players = players


class Player(object):

    name = None
    hand = None

    def __init__(self, name):
        self.name = name


class Table(object):

    walls = None
    current_wall = None