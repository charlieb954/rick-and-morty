#!/usr/bin/env python

"""Tests for `rickandmorty` package."""


from rickandmorty import Characters, Episodes, Locations
from pandas import DataFrame


characters = Characters()
episodes = Episodes()
locations = Locations()


def test_get_character_single():
    character = characters.get_character_single(id=826)
    assert character["name"] == "Butter Robot"


def test_get_episode_single():
    episode = episodes.get_episode_single(3)
    assert episode["name"] == "Anatomy Park"


def test_get_location_single():
    location = locations.get_location_single(id=1)
    assert location["name"] == "Earth (C-137)"


def test_get_character_results():
    _, df = characters.get_character_results(to_pandas=True)
    assert isinstance(df, DataFrame)
