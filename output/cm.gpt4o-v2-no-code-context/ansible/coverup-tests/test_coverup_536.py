# file: lib/ansible/module_utils/common/collections.py:86-97
# asked: {"lines": [86, 94, 95, 97], "branches": [[94, 95], [94, 97]]}
# gained: {"lines": [86, 94, 95, 97], "branches": [[94, 95], [94, 97]]}

import pytest
from ansible.module_utils.common.collections import is_sequence

def test_is_sequence_with_list():
    assert is_sequence([1, 2, 3]) is True

def test_is_sequence_with_tuple():
    assert is_sequence((1, 2, 3)) is True

def test_is_sequence_with_string_include_strings_false():
    assert is_sequence("string", include_strings=False) is False

def test_is_sequence_with_string_include_strings_true():
    assert is_sequence("string", include_strings=True) is True

def test_is_sequence_with_non_sequence():
    assert is_sequence(123) is False

def test_is_sequence_with_bytes_include_strings_false():
    assert is_sequence(b"bytes", include_strings=False) is False

def test_is_sequence_with_bytes_include_strings_true():
    assert is_sequence(b"bytes", include_strings=True) is True
