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
        return 'Mahjong game with: {}'.format(
            ', '.join(map(str, self.players))
        )


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
    """
    Represents the current state of the table including all the walls and keeps
    track of the position in the wall.

    For convenience it has a stack of all stones which are able to be used in
    the game.

    Currently only a full table for the Hong Kong version of the game is
    supported: 144 stones and 4 winds.

    :param list stones: All stones which will be used to build the walls.
    """

    def __init__(self, stones):
        nr_stones = len(stones)
        nr_winds = len(ALL_WINDS)

        assert nr_stones == 144, 'Please supply 144 stones.'
        assert nr_stones % nr_winds == 0, \
            'The number of stones should be dividable by the number of winds.'

        stones_per_wall = int(nr_stones / nr_winds)
        winds = list(ALL_WINDS)
        self.walls = dict()
        start = None
        for i in range(0, nr_stones+1, stones_per_wall):
            stop = i
            if start is not None:
                self.walls[winds.pop(0)] = stones[start:stop]
            start = stop

    walls = None
    current_wall = None
    position_in_wall = None
    death_wall = None
    stone_stack = None
