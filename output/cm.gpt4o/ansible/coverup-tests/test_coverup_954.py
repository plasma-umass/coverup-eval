# file lib/ansible/module_utils/common/collections.py:68-71
# lines [68, 71]
# branches []

import pytest
from ansible.module_utils.common.collections import is_string

def test_is_string_with_text_type():
    assert is_string("test string") == True

def test_is_string_with_binary_type():
    assert is_string(b"test bytes") == True

def test_is_string_with_encrypted_attribute(mocker):
    class MockEncrypted:
        __ENCRYPTED__ = True

    mock_encrypted = MockEncrypted()
    assert is_string(mock_encrypted) == True

def test_is_string_with_non_string():
    assert is_string(12345) == False
    assert is_string([1, 2, 3]) == False
    assert is_string({'key': 'value'}) == False
