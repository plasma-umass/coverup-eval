# file: lib/ansible/parsing/quoting.py:23-24
# asked: {"lines": [23, 24], "branches": []}
# gained: {"lines": [23, 24], "branches": []}

import pytest
from ansible.parsing.quoting import is_quoted

def test_is_quoted_with_double_quotes():
    assert is_quoted('"hello"') == True

def test_is_quoted_with_single_quotes():
    assert is_quoted("'hello'") == True

def test_is_quoted_with_mismatched_quotes():
    assert is_quoted("'hello\"") == False

def test_is_quoted_with_no_quotes():
    assert is_quoted("hello") == False

def test_is_quoted_with_escaped_quote_at_end():
    assert is_quoted('"hello\\"') == False

def test_is_quoted_with_single_character():
    assert is_quoted('"') == False

def test_is_quoted_with_empty_string():
    assert is_quoted('') == False

def test_is_quoted_with_escaped_quote_in_middle():
    assert is_quoted('"he\\"llo"') == True
