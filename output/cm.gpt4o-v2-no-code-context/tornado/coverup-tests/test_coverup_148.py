# file: tornado/escape.py:86-88
# asked: {"lines": [86, 88], "branches": []}
# gained: {"lines": [86, 88], "branches": []}

import pytest
import re
from tornado.escape import squeeze

def test_squeeze_single_space():
    assert squeeze("a  b") == "a b"

def test_squeeze_multiple_spaces():
    assert squeeze("a    b") == "a b"

def test_squeeze_tabs_and_newlines():
    assert squeeze("a\t\nb") == "a b"

def test_squeeze_leading_and_trailing_whitespace():
    assert squeeze("  a  b  ") == "a b"

def test_squeeze_mixed_whitespace():
    assert squeeze("a \t\n  b") == "a b"

def test_squeeze_empty_string():
    assert squeeze("") == ""

def test_squeeze_only_whitespace():
    assert squeeze(" \t\n ") == ""
