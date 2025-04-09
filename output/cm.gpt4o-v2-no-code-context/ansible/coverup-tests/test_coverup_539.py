# file: lib/ansible/parsing/quoting.py:27-31
# asked: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}
# gained: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}

import pytest
from ansible.parsing.quoting import unquote, is_quoted

def test_unquote_with_quotes(monkeypatch):
    def mock_is_quoted(data):
        return True

    monkeypatch.setattr('ansible.parsing.quoting.is_quoted', mock_is_quoted)
    result = unquote('"quoted_string"')
    assert result == 'quoted_string'

def test_unquote_without_quotes(monkeypatch):
    def mock_is_quoted(data):
        return False

    monkeypatch.setattr('ansible.parsing.quoting.is_quoted', mock_is_quoted)
    result = unquote('unquoted_string')
    assert result == 'unquoted_string'
