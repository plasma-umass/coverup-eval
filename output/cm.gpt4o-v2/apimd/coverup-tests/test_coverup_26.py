# file: apimd/parser.py:101-106
# asked: {"lines": [101, 103, 104, 106], "branches": [[103, 104], [103, 106]]}
# gained: {"lines": [101, 103, 104, 106], "branches": [[103, 104], [103, 106]]}

import pytest
from apimd.parser import esc_underscore

def test_esc_underscore_multiple_underscores():
    doc = "example_with_multiple_underscores"
    expected = "example\\_with\\_multiple\\_underscores"
    result = esc_underscore(doc)
    assert result == expected

def test_esc_underscore_single_underscore():
    doc = "example_with_one_underscore"
    expected = "example\\_with\\_one\\_underscore"
    result = esc_underscore(doc)
    assert result == expected

def test_esc_underscore_no_underscore():
    doc = "examplewithnounderscore"
    expected = "examplewithnounderscore"
    result = esc_underscore(doc)
    assert result == expected

def test_esc_underscore_two_underscores():
    doc = "example_with_two_underscores_"
    expected = "example\\_with\\_two\\_underscores\\_"
    result = esc_underscore(doc)
    assert result == expected
