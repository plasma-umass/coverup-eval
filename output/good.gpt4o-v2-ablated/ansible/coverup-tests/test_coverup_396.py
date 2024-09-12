# file: lib/ansible/module_utils/common/collections.py:68-71
# asked: {"lines": [68, 71], "branches": []}
# gained: {"lines": [68, 71], "branches": []}

import pytest
from ansible.module_utils.common.collections import is_string

def test_is_string_with_text_type():
    assert is_string("test string") == True

def test_is_string_with_binary_type():
    assert is_string(b"test bytes") == True

def test_is_string_with_encrypted_attribute():
    class EncryptedString:
        __ENCRYPTED__ = True

    assert is_string(EncryptedString()) == True

def test_is_string_with_non_string():
    assert is_string(12345) == False

def test_is_string_with_sequence_but_not_string():
    assert is_string([1, 2, 3]) == False
