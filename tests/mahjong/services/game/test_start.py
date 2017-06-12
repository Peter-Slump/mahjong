from __future__ import absolute_import

import mock
import unittest

from mahjong.models import Game, Player, WIND_EAST
from tests.mixins import MockTestCaseMixin

import mahjong.services.game


class MahjongGameStartTestCase(MockTestCaseMixin, unittest.TestCase):

    def setUp(self):
        self.game = Game(players=(
            Player(name='John Doe'),
            Player(name='Jane'),
            Player(name='Harvey Peterson'),
            Player(name='Emily Dalson')
        ))

        self.mock_table_create = self.setup_mock(
            'mahjong.services.table.create')
        self.mock_game_choose_first_dealer = self.setup_mock(
            'mahjong.services.game.choose_first_dealer')
        self.mock_player_reset = self.setup_mock(
            'mahjong.services.player.reset')

    def test_service_returns_game(self):
        game = mahjong.services.game.start(game=self.game)

        self.assertEqual(game, self.game)
        self.assertIsInstance(game, Game)

    def test_choose_first_player_is_called(self):
        mahjong.services.game.start(game=self.game)

        self.mock_game_choose_first_dealer.assert_called_once_with(
            game=self.game
        )

    def test_table_is_created(self):
        game = mahjong.services.game.start(game=self.game)

        self.mock_table_create.assert_called_once_with()

        self.assertEqual(game.table, self.mock_table_create.return_value)

    def test_all_players_are_reset(self):
        mahjong.services.game.start(game=self.game)

        calls = [mock.call(player=player) for player in self.game.players]

        self.mock_player_reset.assert_has_calls(calls, True)

    def test_prevailing_wind_is_set(self):
        game = mahjong.services.game.start(game=self.game)

        self.assertEqual(game.prevailing_wind, WIND_EAST)

    def test_error_raised_when_prevailing_wind_is_already_set(self):
        self.game.prevailing_wind = WIND_EAST

        with self.assertRaises(AssertionError) as e:
            mahjong.services.game.start(game=self.game)

        self.assertEqual(e.exception.args[0], 'Game already started')
