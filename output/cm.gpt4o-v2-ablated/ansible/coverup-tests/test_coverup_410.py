# file: lib/ansible/module_utils/splitter.py:33-50
# asked: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 41], [46, 47]]}
# gained: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 41], [46, 47]]}

import pytest

from ansible.module_utils.splitter import _get_quote_state

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

def test_get_quote_state_escaped_single_quote():
    token = "'escaped \\' single quote'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_escaped_double_quote():
    token = '"escaped \\" double quote"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_nested_quotes():
    token = "'nested \"quotes\"'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_unterminated_nested_quotes():
    token = "'unterminated nested \"quotes"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == "'"
