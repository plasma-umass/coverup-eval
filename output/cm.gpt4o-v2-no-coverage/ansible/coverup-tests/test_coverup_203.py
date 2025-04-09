# file: lib/ansible/parsing/splitter.py:106-123
# asked: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 114], [119, 120]]}
# gained: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 114], [119, 120]]}

import pytest

from ansible.parsing.splitter import _get_quote_state

def test_get_quote_state_no_quotes():
    assert _get_quote_state("hello", None) is None

def test_get_quote_state_single_quotes():
    assert _get_quote_state("'hello'", None) is None
    assert _get_quote_state("'hello", None) == "'"
    assert _get_quote_state("he'llo", "'") is None

def test_get_quote_state_double_quotes():
    assert _get_quote_state('"hello"', None) is None
    assert _get_quote_state('"hello', None) == '"'
    assert _get_quote_state('he"llo', '"') is None

def test_get_quote_state_mixed_quotes():
    assert _get_quote_state('"hello\'', None) == '"'
    assert _get_quote_state('\'hello"', None) == "'"

def test_get_quote_state_escaped_quotes():
    assert _get_quote_state('he\\"llo', None) is None
    assert _get_quote_state('he\\\'llo', None) is None

def test_get_quote_state_nested_quotes():
    assert _get_quote_state('"he\'llo"', None) is None
    assert _get_quote_state('\'he"llo\'', None) is None
