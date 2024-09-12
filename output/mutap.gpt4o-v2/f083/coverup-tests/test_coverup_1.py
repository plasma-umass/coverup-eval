# file: f083/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest
from f083 import starts_one_ends

def test_starts_one_ends_with_1():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_with_other():
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800
