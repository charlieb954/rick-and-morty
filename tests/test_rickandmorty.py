#!/usr/bin/env python

"""Tests for `rickandmorty` package."""

import pytest


from rickandmorty import Characters, Episodes, Locations


characters = Characters()
episodes = Episodes()
locations = Locations()

def test_get_character_single():
    character = characters.get_character_single(id=826)
    assert character['name'] == 'Butter Robot'

def test_get_episode_single():
    episode = episodes.get_episode_single(3)
    assert episode['name'] == 'Anatomy Park'

def test_get_location_single():
    location = locations.get_location_single(id=1)
    assert location['name'] == 'Earth (C-137)'