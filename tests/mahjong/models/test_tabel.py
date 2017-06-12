import unittest

from mahjong.models import Table, ALL_WINDS, WIND_EAST, WIND_NORTH, WIND_SOUTH

import mahjong.services.stone


class MahjongTabelModelTestCase(unittest.TestCase):

    def setUp(self):
        self.table = Table(stones=mahjong.services.stone.get_all_shuffled())
        self.table.wall_wind = WIND_EAST  # Open the table

    def test_walls_are_created(self):
        """
        Case: A table is initialized
        Expected: The walls are created
        """
        self.assertEqual(len(self.table.walls), 4)
        for wind, wall in self.table.walls.items():
            self.assertEqual(len(wall), 36)
            self.assertIn(wind, ALL_WINDS)

    def test_get_current_wall(self):
        """
        Case: current wall get requested
        Expected: The wall of the wall wind is returned
        """
        self.assertEqual(
            self.table.walls[self.table.wall_wind],
            self.table.current_wall
        )

    def test_stone_iteration(self):
        """
        Case: we iterate throught the stones of the table
        Expected: we get the same stones as the list we give
        """
        stones = mahjong.services.stone.get_all_shuffled()
        table = Table(stones=stones)
        table.wall_wind = WIND_NORTH  # Last wind
        table.wall_index = 35  # Last stone

        for stone in table:
            self.assertEqual(stone, stones.pop())

    def test_number_stones_returned(self):
        self.table.wall_wind = WIND_NORTH
        self.table.wall_index = 35

        stones = self.table.get_stones(count=3)

        self.assertEqual(len(stones), 3)
