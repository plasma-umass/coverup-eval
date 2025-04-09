# file: isort/format.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest

from isort.format import remove_whitespace

def test_remove_whitespace_basic():
    assert remove_whitespace("a b c") == "abc"

def test_remove_whitespace_with_newline():
    assert remove_whitespace("a\nb\nc") == "abc"

def test_remove_whitespace_with_formfeed():
    assert remove_whitespace("a\x0cb\x0cc") == "abc"

def test_remove_whitespace_with_custom_line_separator():
    assert remove_whitespace("a|b|c", line_separator="|") == "abc"

def test_remove_whitespace_mixed():
    assert remove_whitespace("a \n b \x0c c") == "abc"

def test_remove_whitespace_empty_string():
    assert remove_whitespace("") == ""

def test_remove_whitespace_no_whitespace():
    assert remove_whitespace("abc") == "abc"
