from __future__ import absolute_import

import unittest

import mahjong.services.dice


class MahjongDiceRoll(unittest.TestCase):

    def test_result_is_between_one_and_six(self):
        for _ in range(0, 1000):
            result = mahjong.services.dice.roll()
            self.assertGreaterEqual(result[0], 1)
            self.assertLessEqual(result[0], 6)

    def test_number_results_equal_to_requested(self):
        result = mahjong.services.dice.roll(number_dice=3)
        self.assertEqual(len(result), 3)
