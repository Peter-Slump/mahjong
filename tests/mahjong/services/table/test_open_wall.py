from __future__ import absolute_import

import unittest

from mahjong import models
from mahjong.utils.test.mixins import MockTestCaseMixin

import mahjong.services.stone
import mahjong.services.table


class MahjongTableOpenWall(MockTestCaseMixin, unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.table = mahjong.services.table.create()
        self.table.current_wall = models.WIND_EAST

        self.mock_select_wall_to_open = self.setup_mock(
            'mahjong.services.table._select_wall_to_open')
        self.mock_select_wall_to_open.return_value = self.table

    def test_correct_position_in_same_wall(self):
        dices = (2, 2, 2)  # 6 == position 12 in stack from right
        # One wall has 36 stones == 36 - 12 == 24
        # zero index == 24 - 1 == 23
        table = mahjong.services.table.open_wall(table=self.table,
                                                 dealer_wind=models.WIND_EAST,
                                                 dices=dices)
        self.assertEqual(table.position_in_wall, 23)

    def test_stone_stack_contains_all_stones(self):
        dices = (2, 2, 2)  # 6 == position 12 in stack from right
        # One wall has 36 stones == 36 - 12 == 24
        # zero index == 24 - 1 == 23
        table = mahjong.services.table.open_wall(table=self.table,
                                                 dealer_wind=models.WIND_EAST,
                                                 dices=dices)

        self.assertEqual(len(table.stone_stack), 144)
        self.assertListEqual(
            sorted(table.stone_stack),
            sorted(mahjong.services.stone.get_all_shuffled())
        )
