# file: lib/ansible/module_utils/splitter.py:211-212
# asked: {"lines": [211, 212], "branches": []}
# gained: {"lines": [211, 212], "branches": []}

import pytest
from ansible.module_utils.splitter import is_quoted

def test_is_quoted():
    # Test with double quotes
    assert is_quoted('"data"') == True
    # Test with single quotes
    assert is_quoted("'data'") == True
    # Test with no quotes
    assert is_quoted("data") == False
    # Test with only starting double quote
    assert is_quoted('"data') == False
    # Test with only ending double quote
    assert is_quoted('data"') == False
    # Test with only starting single quote
    assert is_quoted("'data") == False
    # Test with only ending single quote
    assert is_quoted("data'") == False
    # Test with empty string
    assert is_quoted("") == False
    # Test with mismatched quotes
    assert is_quoted('"data\'') == False
    assert is_quoted("'data\"") == False
