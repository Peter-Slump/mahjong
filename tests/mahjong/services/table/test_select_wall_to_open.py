from __future__ import absolute_import

import unittest

from mahjong.models import WIND_EAST, WIND_WEST

import mahjong.services.table


class MahjongTableSelectWallToOpenTestCase(unittest.TestCase):

    def setUp(self):
        self.table = mahjong.services.table.create()

    def test_correct_wall_is_selected(self):
        table = mahjong.services.table._select_wall_to_open(
            table=self.table,
            dealer_wind=WIND_EAST,
            dices=(2, 4, 5)  # 11
        )

        # East > 1
        # South > 2
        # West > 3
        # North > 4
        # East > 5
        # South > 6
        # West > 7
        # North > 8
        # East > 9
        # South > 10
        # West > 11
        self.assertEqual(table.wall_wind, WIND_WEST)

    def test_correct_wall_is_selected_non_east_dealer(self):
        table = mahjong.services.table._select_wall_to_open(
            table=self.table,
            dealer_wind=WIND_WEST,
            dices=(1, 1, 1)  # 3
        )

        # East
        # South
        # West > 1
        # North > 2
        # East > 3
        self.assertEqual(table.wall_wind, WIND_EAST)

    def test_lower_than_four(self):
        table = mahjong.services.table._select_wall_to_open(
            table=self.table,
            dealer_wind=WIND_EAST,
            dices=(1, 1, 1)  # 3
        )

        # East > 1
        # South > 2
        # West > 3
        self.assertEqual(table.wall_wind, WIND_WEST)
