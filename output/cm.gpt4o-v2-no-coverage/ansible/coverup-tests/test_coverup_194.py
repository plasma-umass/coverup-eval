# file: lib/ansible/module_utils/splitter.py:33-50
# asked: {"lines": [33, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 41], [46, 47]]}
# gained: {"lines": [33, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [42, 43], [42, 44], [44, 41], [44, 45], [45, 46], [45, 49], [46, 41], [46, 47]]}

import pytest

from ansible.module_utils.splitter import _get_quote_state

def test_get_quote_state_no_quotes():
    assert _get_quote_state("hello", None) is None

def test_get_quote_state_single_quotes():
    assert _get_quote_state("'hello'", None) is None

def test_get_quote_state_double_quotes():
    assert _get_quote_state('"hello"', None) is None

def test_get_quote_state_unterminated_single_quote():
    assert _get_quote_state("'hello", None) == "'"

def test_get_quote_state_unterminated_double_quote():
    assert _get_quote_state('"hello', None) == '"'

def test_get_quote_state_escaped_single_quote():
    assert _get_quote_state("\\'hello\\'", None) is None

def test_get_quote_state_escaped_double_quote():
    assert _get_quote_state('\\"hello\\"', None) is None

def test_get_quote_state_mixed_quotes():
    assert _get_quote_state("'hello\"", None) == "'"

def test_get_quote_state_mixed_quotes_terminated():
    assert _get_quote_state("'hello\"'", None) is None

def test_get_quote_state_nested_quotes():
    assert _get_quote_state("'he\"llo'", None) is None

def test_get_quote_state_nested_unterminated_quotes():
    assert _get_quote_state("'he\"llo", None) == "'"
