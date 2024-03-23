# file lib/ansible/parsing/quoting.py:23-24
# lines [23, 24]
# branches []

import pytest
from ansible.parsing.quoting import is_quoted

def test_is_quoted():
    assert is_quoted('""') == True
    assert is_quoted("''") == True
    assert is_quoted('"Some string"') == True
    assert is_quoted("'Some other string'") == True
    assert is_quoted('Not quoted') == False
    assert is_quoted('"Mismatched\'') == False
    assert is_quoted('a') == False
    assert is_quoted('"This is a test\\"') == False
    assert is_quoted("'Another test\\'") == False
