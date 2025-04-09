# file: lib/ansible/parsing/quoting.py:27-31
# asked: {"lines": [30], "branches": [[29, 30]]}
# gained: {"lines": [30], "branches": [[29, 30]]}

import pytest
from ansible.parsing.quoting import unquote

def test_unquote_no_quotes():
    assert unquote("noquotes") == "noquotes"

def test_unquote_single_quotes():
    assert unquote("'singlequotes'") == "singlequotes"

def test_unquote_double_quotes():
    assert unquote('"doublequotes"') == "doublequotes"

def test_unquote_mismatched_quotes():
    assert unquote("'mismatched\"") == "'mismatched\""

def test_unquote_escaped_quotes():
    assert unquote("\"escaped\\\"quotes\"") == "escaped\\\"quotes"
