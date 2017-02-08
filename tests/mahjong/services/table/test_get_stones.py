from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.game
import mahjong.services.table


class MahjongTableGetStones(unittest.TestCase):

    def setUp(self):
        self.game = mahjong.services.game.create(players=[
            models.Player(name='John'),
            models.Player(name='Jane'),
            models.Player(name='Charles'),
            models.Player(name='Chris'),
        ])
        mahjong.services.game.start(game=self.game)

        self.table, dice = mahjong.services.table.open_wall(game=self.game)

    def test_get_last_tone_of_stack(self):
        expected_stone = self.table.stone_stack[-1]

        stone = mahjong.services.table.get_stones(table=self.table,
                                                  nr_stones=1)

        self.assertTupleEqual((expected_stone,), stone)

    def test_number_stones_returned(self):
        stone = mahjong.services.table.get_stones(table=self.table,
                                                  nr_stones=3)

        self.assertEqual(len(stone), 3)

    def test_last_stones_get_returned(self):
        expected_stones = self.table.stone_stack[-3:]

        stones = mahjong.services.table.get_stones(table=self.table,
                                                   nr_stones=3)

        self.assertTupleEqual(tuple(reversed(expected_stones)), stones)
