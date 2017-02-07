from __future__ import absolute_import

import unittest

from mahjong import models

from tests.utils.mixins import MockTestCaseMixin

import mahjong.services.table
import mahjong.services.stone


class MahjongTableCreateTestCase(MockTestCaseMixin, unittest.TestCase):

    def test_table_returned(self):
        table = mahjong.services.table.create()

        self.assertIsInstance(table, models.Table)

    def test_walls_created(self):
        table = mahjong.services.table.create()

        self.assertEqual(len(table.walls[models.WIND_EAST]), 36)
        self.assertEqual(len(table.walls[models.WIND_SOUTH]), 36)
        self.assertEqual(len(table.walls[models.WIND_WEST]), 36)
        self.assertEqual(len(table.walls[models.WIND_NORTH]), 36)

    def test_all_stones_available(self):
        table = mahjong.services.table.create()

        self.assertListEqual(
            sorted(
                table.walls[models.WIND_EAST] +
                table.walls[models.WIND_SOUTH] +
                table.walls[models.WIND_WEST] +
                table.walls[models.WIND_NORTH]
            ),
            sorted(
                mahjong.services.stone.get_all_shuffled()
            )
        )
