# file: apimd/parser.py:101-106
# asked: {"lines": [101, 103, 104, 106], "branches": [[103, 104], [103, 106]]}
# gained: {"lines": [101, 103, 104, 106], "branches": [[103, 104], [103, 106]]}

import pytest
from apimd.parser import esc_underscore

def test_esc_underscore_multiple_underscores():
    doc = "this_is_a_test"
    expected = "this\\_is\\_a\\_test"
    result = esc_underscore(doc)
    assert result == expected

def test_esc_underscore_single_underscore():
    doc = "this_is"
    expected = "this_is"
    result = esc_underscore(doc)
    assert result == expected

def test_esc_underscore_no_underscore():
    doc = "thisis"
    expected = "thisis"
    result = esc_underscore(doc)
    assert result == expected
