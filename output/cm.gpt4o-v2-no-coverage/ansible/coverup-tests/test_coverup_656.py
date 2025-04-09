# file: lib/ansible/parsing/quoting.py:27-31
# asked: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}
# gained: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}

import pytest
from ansible.parsing.quoting import unquote

def test_unquote_with_quotes():
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'

def test_unquote_without_quotes():
    assert unquote('hello') == 'hello'
    assert unquote('"hello') == '"hello'
    assert unquote('hello"') == 'hello"'
    assert unquote("'hello") == "'hello"
    assert unquote("hello'") == "hello'"

def test_unquote_escaped_quotes():
    assert unquote('"hello\\"') == '"hello\\"'
    assert unquote("'hello\\'") == "'hello\\'"

def test_unquote_empty_string():
    assert unquote('') == ''
