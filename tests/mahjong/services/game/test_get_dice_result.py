from __future__ import absolute_import

import unittest

import mahjong.services.game


class MahjongGameGetDiceResult(unittest.TestCase):

    def test_result_is_between_one_and_six(self):
        for _ in range(0, 1000):
            result = mahjong.services.game.get_dice_result()
            self.assertGreaterEqual(result[0], 1)
            self.assertLessEqual(result[0], 6)

    def test_number_results_equal_to_requested(self):
        result = mahjong.services.game.get_dice_result(nr_dices=3)
        self.assertEqual(len(result), 3)
