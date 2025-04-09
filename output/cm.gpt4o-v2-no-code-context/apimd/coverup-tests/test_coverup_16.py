# file: apimd/parser.py:51-53
# asked: {"lines": [51, 53], "branches": []}
# gained: {"lines": [51, 53], "branches": []}

import pytest
from apimd.parser import parent

def test_parent_single_level():
    result = parent("a.b.c")
    assert result == "a.b"

def test_parent_multiple_levels():
    result = parent("a.b.c.d", level=2)
    assert result == "a.b"

def test_parent_no_split():
    result = parent("a", level=1)
    assert result == "a"

def test_parent_level_zero():
    result = parent("a.b.c", level=0)
    assert result == "a.b.c"
