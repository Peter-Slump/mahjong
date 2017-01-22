from __future__ import absolute_import

import unittest

from collections import defaultdict

from mahjong import stones

import mahjong.services.table


class MahjongTableGetShuffledStonesTestCase(unittest.TestCase):

    def test_number_of_returned_items_is_correct(self):
        result = mahjong.services.table.get_shuffled_stones()

        self.assertEqual(len(result), 144)

    def test_results_differs(self):

        first_result = mahjong.services.table.get_shuffled_stones()
        second_result = mahjong.services.table.get_shuffled_stones()

        self.assertNotEqual(first_result, second_result)

        self.assertListEqual(sorted(first_result), sorted(second_result))

    def test_all_stones_available_in_correct_amount(self):
        result = mahjong.services.table.get_shuffled_stones()

        result_dict = defaultdict(lambda: 0)

        for stone in result:
            result_dict[stone] += 1

        self.assertEqual(result_dict[stones.DOTS_ONE], 4)
        self.assertEqual(result_dict[stones.DOTS_TWO], 4)
        self.assertEqual(result_dict[stones.DOTS_THREE], 4)
        self.assertEqual(result_dict[stones.DOTS_FOUR], 4)
        self.assertEqual(result_dict[stones.DOTS_FIVE], 4)
        self.assertEqual(result_dict[stones.DOTS_SIX], 4)
        self.assertEqual(result_dict[stones.DOTS_SEVEN], 4)
        self.assertEqual(result_dict[stones.DOTS_EIGHT], 4)
        self.assertEqual(result_dict[stones.DOTS_NINE], 4)

        self.assertEqual(result_dict[stones.BAMBOO_ONE], 4)
        self.assertEqual(result_dict[stones.BAMBOO_TWO], 4)
        self.assertEqual(result_dict[stones.BAMBOO_THREE], 4)
        self.assertEqual(result_dict[stones.BAMBOO_FOUR], 4)
        self.assertEqual(result_dict[stones.BAMBOO_FIVE], 4)
        self.assertEqual(result_dict[stones.BAMBOO_SIX], 4)
        self.assertEqual(result_dict[stones.BAMBOO_SEVEN], 4)
        self.assertEqual(result_dict[stones.BAMBOO_EIGHT], 4)
        self.assertEqual(result_dict[stones.BAMBOO_NINE], 4)

        self.assertEqual(result_dict[stones.CHARACTERS_ONE], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_TWO], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_THREE], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_FOUR], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_FIVE], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_SIX], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_SEVEN], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_EIGHT], 4)
        self.assertEqual(result_dict[stones.CHARACTERS_NINE], 4)

        self.assertEqual(result_dict[stones.WIND_EAST], 4)
        self.assertEqual(result_dict[stones.WIND_SOUTH], 4)
        self.assertEqual(result_dict[stones.WIND_WEST], 4)
        self.assertEqual(result_dict[stones.WIND_NORTH], 4)

        self.assertEqual(result_dict[stones.DRAGON_WHITE], 4)
        self.assertEqual(result_dict[stones.DRAGON_RED], 4)
        self.assertEqual(result_dict[stones.DRAGON_GREEN], 4)

        self.assertEqual(result_dict[stones.SEASONS_WINTER], 1)
        self.assertEqual(result_dict[stones.SEASONS_AUTUMN], 1)
        self.assertEqual(result_dict[stones.SEASONS_SUMMER], 1)
        self.assertEqual(result_dict[stones.SEASONS_SPRING], 1)

        self.assertEqual(result_dict[stones.FLOWERS_BAMBOO], 1)
        self.assertEqual(result_dict[stones.FLOWERS_CHRYSANTHEMUM], 1)
        self.assertEqual(result_dict[stones.FLOWERS_ORCHID], 1)
        self.assertEqual(result_dict[stones.FLOWERS_PLUM], 1)
