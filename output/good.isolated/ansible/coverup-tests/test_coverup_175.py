# file lib/ansible/parsing/splitter.py:106-123
# lines [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123]
# branches ['114->115', '114->123', '115->116', '115->117', '117->114', '117->118', '118->119', '118->122', '119->114', '119->120']

import pytest

from ansible.parsing.splitter import _get_quote_state

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_get_quote_state_unterminated_single_quote(cleanup):
    token = "This is an unterminated 'string"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == "'", "The function should return a single quote indicating unterminated string"

def test_get_quote_state_unterminated_double_quote(cleanup):
    token = 'This is an unterminated "string'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"', "The function should return a double quote indicating unterminated string"

def test_get_quote_state_terminated_quotes(cleanup):
    token = 'This is a "properly terminated" string'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "The function should return None for a terminated string"

def test_get_quote_state_escaped_quote(cleanup):
    token = 'This is a string with an escaped \\" quote'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "The function should return None when the quote is escaped"

def test_get_quote_state_multiple_quotes(cleanup):
    token = 'This "is" a \'string\' with "multiple" quotes'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "The function should return None when all quotes are terminated"

def test_get_quote_state_nested_quotes(cleanup):
    token = 'This "is \'a\' nested" quote'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None, "The function should return None for properly nested quotes"

def test_get_quote_state_mixed_unterminated_quotes(cleanup):
    token = 'This "is an unterminated string with a \' quote inside'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"', "The function should return the double quote indicating unterminated string"
