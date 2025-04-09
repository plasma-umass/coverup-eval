# file lib/ansible/parsing/quoting.py:23-24
# lines [23, 24]
# branches []

import pytest
from ansible.parsing.quoting import is_quoted

def test_is_quoted():
    # Test cases where the function should return True
    assert is_quoted('"hello"') == True
    assert is_quoted("'world'") == True
    assert is_quoted('"a"') == True
    assert is_quoted("'b'") == True

    # Test cases where the function should return False
    assert is_quoted('hello') == False
    assert is_quoted('"hello') == False
    assert is_quoted('hello"') == False
    assert is_quoted("'hello") == False
    assert is_quoted('hello\'') == False
    assert is_quoted('') == False
    assert is_quoted('"') == False
    assert is_quoted("'") == False
    assert is_quoted('""') == True  # Edge case: empty string within quotes
    assert is_quoted("''") == True  # Edge case: empty string within quotes
    assert is_quoted('"hello\\"') == False  # Edge case: escaped quote at the end
    assert is_quoted("'hello\\'") == False  # Edge case: escaped quote at the end
