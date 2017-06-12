from __future__ import absolute_import

import unittest

from mahjong.models import Table, WIND_EAST, WIND_NORTH, WIND_SOUTH, WIND_WEST
from tests.mixins import MockTestCaseMixin

import mahjong.services.stone
import mahjong.services.table


class MahjongTableCreateTestCase(MockTestCaseMixin, unittest.TestCase):

    def test_table_returned(self):
        table = mahjong.services.table.create()

        self.assertIsInstance(table, Table)

    def test_walls_created(self):
        table = mahjong.services.table.create()

        self.assertEqual(len(table.walls[WIND_EAST]), 36)
        self.assertEqual(len(table.walls[WIND_SOUTH]), 36)
        self.assertEqual(len(table.walls[WIND_WEST]), 36)
        self.assertEqual(len(table.walls[WIND_NORTH]), 36)

    def test_all_stones_available(self):
        table = mahjong.services.table.create()

        self.assertListEqual(
            sorted(
                table.walls[WIND_EAST] +
                table.walls[WIND_SOUTH] +
                table.walls[WIND_WEST] +
                table.walls[WIND_NORTH]
            ),
            sorted(
                mahjong.services.stone.get_all_shuffled()
            )
        )
