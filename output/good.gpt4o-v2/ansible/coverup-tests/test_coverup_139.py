# file: lib/ansible/parsing/splitter.py:106-123
# asked: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 114], [119, 120]]}
# gained: {"lines": [106, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123], "branches": [[114, 115], [114, 123], [115, 116], [115, 117], [117, 114], [117, 118], [118, 119], [118, 122], [119, 114], [119, 120]]}

import pytest
from ansible.parsing.splitter import _get_quote_state

def test_get_quote_state_no_quotes():
    assert _get_quote_state("no quotes here", None) is None

def test_get_quote_state_single_quotes():
    assert _get_quote_state("'single quotes'", None) is None

def test_get_quote_state_double_quotes():
    assert _get_quote_state('"double quotes"', None) is None

def test_get_quote_state_unterminated_single_quote():
    assert _get_quote_state("'unterminated single quote", None) == "'"

def test_get_quote_state_unterminated_double_quote():
    assert _get_quote_state('"unterminated double quote', None) == '"'

def test_get_quote_state_escaped_single_quote():
    assert _get_quote_state(r"\'escaped single quote\'", None) is None

def test_get_quote_state_escaped_double_quote():
    assert _get_quote_state(r'\"escaped double quote\"', None) is None

def test_get_quote_state_mixed_quotes():
    assert _get_quote_state("'mixed \"quotes\"'", None) is None

def test_get_quote_state_mixed_unterminated_quotes():
    assert _get_quote_state("'mixed \"quotes", None) == "'"
