# file: f016/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f016 import count_distinct_characters

def test_count_distinct_characters():
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("World") == 5
    assert count_distinct_characters("Python") == 6
    assert count_distinct_characters("Mississippi") == 4
    assert count_distinct_characters("") == 0
