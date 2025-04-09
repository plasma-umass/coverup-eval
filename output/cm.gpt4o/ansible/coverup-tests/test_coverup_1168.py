# file lib/ansible/parsing/splitter.py:106-123
# lines [118, 119, 120, 122]
# branches ['117->118', '118->119', '118->122', '119->114', '119->120']

import pytest
from ansible.parsing.splitter import _get_quote_state

def test_get_quote_state_unterminated_quote():
    # Test case where the quote is unterminated
    token = 'unterminated "quote'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"', "Expected unterminated quote to return the quote character"

def test_get_quote_state_terminated_quote():
    # Test case where the quote is terminated
    token = 'terminated "quote"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "Expected terminated quote to return None"

def test_get_quote_state_escaped_quote():
    # Test case where the quote is escaped
    token = 'escaped \\"quote"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"', "Expected escaped quote to return the quote character"

def test_get_quote_state_single_quote():
    # Test case with single quotes
    token = "single 'quote'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "Expected single quote to return None"

def test_get_quote_state_unterminated_single_quote():
    # Test case where the single quote is unterminated
    token = "unterminated 'quote"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == "'", "Expected unterminated single quote to return the quote character"
