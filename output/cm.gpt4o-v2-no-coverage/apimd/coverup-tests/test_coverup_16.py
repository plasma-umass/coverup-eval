# file: apimd/parser.py:51-53
# asked: {"lines": [51, 53], "branches": []}
# gained: {"lines": [51, 53], "branches": []}

import pytest
from apimd.parser import parent

def test_parent_single_level():
    assert parent("a.b.c") == "a.b"

def test_parent_multiple_levels():
    assert parent("a.b.c.d", level=2) == "a.b"

def test_parent_no_split():
    assert parent("abc") == "abc"

def test_parent_level_zero():
    assert parent("a.b.c", level=0) == "a.b.c"
