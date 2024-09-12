# file: f015/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f015 import string_sequence

def test_string_sequence():
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "0 1"
    assert string_sequence(5) == "0 1 2 3 4 5"
