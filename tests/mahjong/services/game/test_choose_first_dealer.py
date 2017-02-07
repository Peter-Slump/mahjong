from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.game


class MahjongGameChooseFirstDealerTestCase(unittest.TestCase):

    def setUp(self):
        self.game = models.Game(players=[
            models.Player(name='John Doe'),
            models.Player(name='Jane'),
            models.Player(name='Harvey Peterson'),
            models.Player(name='Emily Dalson')
        ])

    def test_current_dealer_is_one_of_the_players(self):
        game = mahjong.services.game.choose_first_dealer(game=self.game)

        assert game.current_dealer in self.game.players

    def test_service_returns_game(self):
        game = mahjong.services.game.choose_first_dealer(game=self.game)

        self.assertEqual(game, self.game)

    def test_error_raised_when_no_players_are_set(self):
        self.game.players = None

        with self.assertRaises(AssertionError) as e:
            mahjong.services.game.choose_first_dealer(game=self.game)

        self.assertEqual(e.exception.args[0], 'Please set players first')

    def test_error_raises_when_dealer_alread_set(self):
        self.game.current_dealer = self.game.players[0]

        with self.assertRaises(AssertionError) as e:
            mahjong.services.game.choose_first_dealer(self.game)

        self.assertEqual(e.exception.args[0], 'Dealer already set')
