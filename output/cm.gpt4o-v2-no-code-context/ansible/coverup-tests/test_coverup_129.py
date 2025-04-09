# file: lib/ansible/parsing/splitter.py:106-123
# asked: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 114], [119, 120]]}
# gained: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 120]]}

import pytest
from ansible.parsing.splitter import _get_quote_state

def test_get_quote_state_no_quotes():
    token = "noquotes"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_single_quotes():
    token = "'single quotes'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_double_quotes():
    token = '"double quotes"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_unterminated_single_quote():
    token = "'unterminated single quote"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == "'"

def test_get_quote_state_unterminated_double_quote():
    token = '"unterminated double quote'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"'

def test_get_quote_state_escaped_quote():
    token = r'\"escaped double quote\"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_escaped_single_quote():
    token = r"\'escaped single quote\'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None
