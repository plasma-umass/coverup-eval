# file: f017/__init__.py:4-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest
from f017 import parse_music

def test_parse_music():
    # Test with a valid music string
    music_string = "o o| .|"
    expected_output = [4, 2, 1]
    assert parse_music(music_string) == expected_output

    # Test with an empty string
    music_string = ""
    expected_output = []
    assert parse_music(music_string) == expected_output

    # Test with a string containing only spaces
    music_string = "   "
    expected_output = []
    assert parse_music(music_string) == expected_output

    # Test with a string containing invalid notes
    music_string = "x y z"
    with pytest.raises(KeyError):
        parse_music(music_string)
