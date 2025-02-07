# file: lib/ansible/module_utils/common/json.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest

# Assuming the _is_unsafe function is part of a module named 'json_utils'
from ansible.module_utils.common.json import _is_unsafe

def test_is_unsafe_with_unsafe_and_not_encrypted():
    class TestValue:
        __UNSAFE__ = True
        __ENCRYPTED__ = False

    value = TestValue()
    assert _is_unsafe(value) is True

def test_is_unsafe_with_unsafe_and_encrypted():
    class TestValue:
        __UNSAFE__ = True
        __ENCRYPTED__ = True

    value = TestValue()
    assert _is_unsafe(value) is False

def test_is_unsafe_without_unsafe():
    class TestValue:
        __UNSAFE__ = False
        __ENCRYPTED__ = False

    value = TestValue()
    assert _is_unsafe(value) is False

def test_is_unsafe_without_unsafe_attribute():
    class TestValue:
        __ENCRYPTED__ = False

    value = TestValue()
    assert _is_unsafe(value) is False

def test_is_unsafe_without_encrypted_attribute():
    class TestValue:
        __UNSAFE__ = True

    value = TestValue()
    assert _is_unsafe(value) is True

def test_is_unsafe_without_any_attributes():
    class TestValue:
        pass

    value = TestValue()
    assert _is_unsafe(value) is False
