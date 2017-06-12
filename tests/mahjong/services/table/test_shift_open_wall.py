from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.table

@unittest.skip
class MahjongTableShiftOpenWall(unittest.TestCase):

    def setUp(self):
        self.table = mahjong.services.table.create()
        self.table.wall_wind = models.WIND_SOUTH

    def test_wall_is_shifted_to_right_set(self):
        table = mahjong.services.table._shift_open_wall(table=self.table)

        self.assertEqual(table.wall_wind, models.WIND_EAST)

    def test_table_get_returned(self):
        table = mahjong.services.table._shift_open_wall(table=self.table)

        self.assertEqual(self.table, table)
        self.assertIsInstance(self.table, models.Table)

    def test_last_wall_is_selected_when_current_wall_is_first(self):
        self.table.wall_wind = models.WIND_EAST

        table = mahjong.services.table._shift_open_wall(table=self.table)

        self.assertEqual(table.wall_wind, models.WIND_NORTH)
