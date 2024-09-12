# file: lib/ansible/module_utils/splitter.py:33-50
# asked: {"lines": [33, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 41], [46, 47]]}
# gained: {"lines": [33, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 47]]}

import pytest

def test_get_quote_state_no_quotes():
    from ansible.module_utils.splitter import _get_quote_state
    token = "This is a test"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_single_quotes():
    from ansible.module_utils.splitter import _get_quote_state
    token = "This is a 'test'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_double_quotes():
    from ansible.module_utils.splitter import _get_quote_state
    token = 'This is a "test"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_unterminated_single_quote():
    from ansible.module_utils.splitter import _get_quote_state
    token = "This is a 'test"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == "'"

def test_get_quote_state_unterminated_double_quote():
    from ansible.module_utils.splitter import _get_quote_state
    token = 'This is a "test'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result == '"'

def test_get_quote_state_escaped_quote():
    from ansible.module_utils.splitter import _get_quote_state
    token = 'This is a \\"test\\"'
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None

def test_get_quote_state_escaped_single_quote():
    from ansible.module_utils.splitter import _get_quote_state
    token = "This is a \\'test\\'"
    quote_char = None
    result = _get_quote_state(token, quote_char)
    assert result is None
