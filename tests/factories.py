from __future__ import absolute_import

import factory

from mahjong import models


class PlayerFactory(factory.Factory):

    class Meta:
        model = models.Player

    name = factory.Faker('name')


class GameFactory(factory.Factory):

    class Meta:
        model = models.Game

    players = factory.LazyAttribute(
        lambda n: [PlayerFactory() for _ in range(0, 4)]
    )
    current_dealer = factory.Iterator(models.ALL_WINDS)
    prevailing_wind = factory.Iterator(models.ALL_WINDS)
    table = factory.SubFactory('tests.factories.TableFactory')


class TableFactory(factory.Factory):

    class Meta:
        model = models.Table

    stones = []