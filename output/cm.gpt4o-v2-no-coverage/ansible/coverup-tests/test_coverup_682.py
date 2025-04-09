# file: lib/ansible/module_utils/common/collections.py:86-97
# asked: {"lines": [86, 94, 95, 97], "branches": [[94, 95], [94, 97]]}
# gained: {"lines": [86, 94, 95, 97], "branches": [[94, 95], [94, 97]]}

import pytest
from ansible.module_utils.common.collections import is_sequence, is_string
from collections.abc import Sequence

def test_is_sequence_with_list():
    assert is_sequence([1, 2, 3]) == True

def test_is_sequence_with_tuple():
    assert is_sequence((1, 2, 3)) == True

def test_is_sequence_with_string():
    assert is_sequence("string") == False

def test_is_sequence_with_string_included():
    assert is_sequence("string", include_strings=True) == True

def test_is_sequence_with_bytes():
    assert is_sequence(b"bytes") == False

def test_is_sequence_with_bytes_included():
    assert is_sequence(b"bytes", include_strings=True) == True

def test_is_sequence_with_non_sequence():
    assert is_sequence(123) == False

def test_is_sequence_with_custom_sequence():
    class CustomSequence(Sequence):
        def __getitem__(self, index):
            return index
        def __len__(self):
            return 1
    assert is_sequence(CustomSequence()) == True

def test_is_string_with_text_type():
    assert is_string("text") == True

def test_is_string_with_binary_type():
    assert is_string(b"binary") == True

def test_is_string_with_non_string():
    assert is_string(123) == False

def test_is_string_with_encrypted_attr():
    class EncryptedString:
        __ENCRYPTED__ = True
    assert is_string(EncryptedString()) == True
