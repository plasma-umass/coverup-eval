# file: lib/ansible/module_utils/common/json.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest

from ansible.module_utils.common.json import _is_unsafe

class UnsafeObject:
    __UNSAFE__ = True
    __ENCRYPTED__ = False

class SafeObject:
    __UNSAFE__ = False
    __ENCRYPTED__ = False

class EncryptedObject:
    __UNSAFE__ = True
    __ENCRYPTED__ = True

def test_is_unsafe_with_unsafe_object():
    obj = UnsafeObject()
    assert _is_unsafe(obj) == True

def test_is_unsafe_with_safe_object():
    obj = SafeObject()
    assert _is_unsafe(obj) == False

def test_is_unsafe_with_encrypted_object():
    obj = EncryptedObject()
    assert _is_unsafe(obj) == False

def test_is_unsafe_with_non_object():
    obj = "string"
    assert _is_unsafe(obj) == False
