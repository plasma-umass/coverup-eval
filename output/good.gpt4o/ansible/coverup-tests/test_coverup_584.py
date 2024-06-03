# file lib/ansible/module_utils/common/collections.py:86-97
# lines [86, 94, 95, 97]
# branches ['94->95', '94->97']

import pytest
from unittest.mock import patch
from ansible.module_utils.common.collections import is_sequence

def test_is_sequence_with_string():
    assert not is_sequence("test_string")

def test_is_sequence_with_string_included():
    assert is_sequence("test_string", include_strings=True)

def test_is_sequence_with_list():
    assert is_sequence([1, 2, 3])

def test_is_sequence_with_tuple():
    assert is_sequence((1, 2, 3))

def test_is_sequence_with_non_sequence():
    assert not is_sequence(123)

def test_is_sequence_with_bytes():
    assert not is_sequence(b'test_bytes')

def test_is_sequence_with_bytes_included():
    assert is_sequence(b'test_bytes', include_strings=True)
