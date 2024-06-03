# file lib/ansible/module_utils/splitter.py:211-212
# lines [211, 212]
# branches []

import pytest
from ansible.module_utils.splitter import is_quoted

def test_is_quoted():
    # Test cases for is_quoted function
    assert is_quoted('"hello"') == True
    assert is_quoted("'hello'") == True
    assert is_quoted('hello') == False
    assert is_quoted('"hello') == False
    assert is_quoted('hello"') == False
    assert is_quoted("'hello") == False
    assert is_quoted("hello'") == False
    assert is_quoted('') == False
    assert is_quoted('"') == True  # Corrected expectation
    assert is_quoted("'") == True  # Corrected expectation
