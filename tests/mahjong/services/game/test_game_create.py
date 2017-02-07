from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.game


class MahjongGameCreateTestCase(unittest.TestCase):

    def setUp(self):
        self.players = [
            models.Player(name='John Doe'),
            models.Player(name='Jane'),
            models.Player(name='Harvey Peterson'),
            models.Player(name='Emily Dalson')
        ]

    def test_return_game_model(self):
        result = mahjong.services.game.create(players=self.players)

        self.assertIsInstance(result, models.Game)

    def test_players_assigned(self):
        game = mahjong.services.game.create(players=self.players)

        self.assertEqual(self.players, game.players)

    def test_not_all_players_are_correct_type(self):
        players = self.players[0:3] + [models.Game]

        with self.assertRaises(AssertionError) as e:
            mahjong.services.game.create(players=players)

        self.assertEqual(e.exception.args[0],
                         'Players should be of type Player')

    def test_players_length_not_correct_length(self):

        with self.assertRaises(AssertionError) as e:
            mahjong.services.game.create(players=self.players[0:2])

        self.assertEqual(e.exception.args[0], 'Please supply 4 players')
