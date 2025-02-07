# file: lib/ansible/module_utils/splitter.py:211-212
# asked: {"lines": [211, 212], "branches": []}
# gained: {"lines": [211, 212], "branches": []}

import pytest
from ansible.module_utils.splitter import is_quoted

def test_is_quoted_double_quotes():
    assert is_quoted('"data"') == True

def test_is_quoted_single_quotes():
    assert is_quoted("'data'") == True

def test_is_quoted_no_quotes():
    assert is_quoted("data") == False

def test_is_quoted_mismatched_quotes():
    assert is_quoted('"data\'') == False
    assert is_quoted("'data\"") == False

def test_is_quoted_empty_string():
    assert is_quoted("") == False
