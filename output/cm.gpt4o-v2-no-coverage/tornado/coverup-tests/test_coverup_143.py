# file: tornado/escape.py:86-88
# asked: {"lines": [86, 88], "branches": []}
# gained: {"lines": [86, 88], "branches": []}

import pytest
import re
from tornado.escape import squeeze

def test_squeeze_single_whitespace():
    assert squeeze("hello  world") == "hello world"

def test_squeeze_multiple_whitespace():
    assert squeeze("hello   world") == "hello world"

def test_squeeze_tabs():
    assert squeeze("hello\tworld") == "hello world"

def test_squeeze_newlines():
    assert squeeze("hello\nworld") == "hello world"

def test_squeeze_mixed_whitespace():
    assert squeeze("hello \t\nworld") == "hello world"

def test_squeeze_leading_trailing_whitespace():
    assert squeeze("  hello world  ") == "hello world"

def test_squeeze_no_whitespace():
    assert squeeze("helloworld") == "helloworld"

def test_squeeze_empty_string():
    assert squeeze("") == ""

def test_squeeze_only_whitespace():
    assert squeeze(" \t\n") == ""
