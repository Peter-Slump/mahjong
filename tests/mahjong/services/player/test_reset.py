from __future__ import absolute_import

import unittest

from mahjong import models

import mahjong.services.player


class MahjongPlayerResetTestCase(unittest.TestCase):

    def setUp(self):
        self.player = models.Player(name='John Doe')

    def test_hand_is_set_to_none(self):
        self.player.hand = []

        player = mahjong.services.player.reset(player=self.player)
        self.assertIsNone(player.hand)

    def test_player_is_returned(self):
        player = mahjong.services.player.reset(player=self.player)

        self.assertEqual(player, self.player)
        self.assertIsInstance(player, models.Player)
