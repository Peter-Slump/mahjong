from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.table


class MahjongTableGetStones(unittest.TestCase):

    def setUp(self):
        self.table = mahjong.services.table.open_wall(
            table=mahjong.services.table.create(),
            dealer_wind=models.WIND_EAST,
            dices=(1,1,1)
        )

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
