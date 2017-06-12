from __future__ import absolute_import

import unittest

from mahjong.models import Game, Player, WIND_EAST
from tests.mixins import MockTestCaseMixin

import mahjong.services.game
import mahjong.services.stone
import mahjong.services.table


class MahjongTableOpenWall(MockTestCaseMixin, unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.game = mahjong.services.game.create(players=[
            Player(name='John'),
            Player(name='Jane'),
            Player(name='Charles'),
            Player(name='Chris'),
        ])
        mahjong.services.game.start(game=self.game)

        self.mock_select_wall_to_open = self.setup_mock(
            'mahjong.services.table._select_wall_to_open')
        self.game.table.wall_wind = WIND_EAST
        self.mock_select_wall_to_open.return_value = self.game.table

        self.mock_dice_roll = self.setup_mock('mahjong.services.dice.roll')
        self.mock_dice_roll.return_value = (2, 2, 2)

    def test_correct_position_in_same_wall(self):
        # 6 == position 12 in stack from right
        # One wall has 36 stones == 36 - 12 == 24
        # zero index == 24 - 1 == 23
        table, dice = mahjong.services.table.open_wall(game=self.game)
        self.assertEqual(table.wall_index, 23)

    def test_stone_stack_contains_all_stones(self):
        # 6 == position 12 in stack from right
        # One wall has 36 stones == 36 - 12 == 24
        # zero index == 24 - 1 == 23
        table, dice = mahjong.services.table.open_wall(game=self.game)

        self.assertEqual(len(table.stone_stack), 144)
        self.assertListEqual(
            sorted(table.stone_stack),
            sorted(mahjong.services.stone.get_all_shuffled())
        )
