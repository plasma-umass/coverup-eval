# file: lib/ansible/module_utils/common/json.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest

from ansible.module_utils.common.json import _is_vault

def test_is_vault_with_encrypted_attribute():
    class Encrypted:
        __ENCRYPTED__ = True

    value = Encrypted()
    assert _is_vault(value) is True

def test_is_vault_without_encrypted_attribute():
    class NotEncrypted:
        pass

    value = NotEncrypted()
    assert _is_vault(value) is False

def test_is_vault_with_encrypted_attribute_false():
    class EncryptedFalse:
        __ENCRYPTED__ = False

    value = EncryptedFalse()
    assert _is_vault(value) is False

def test_is_vault_with_non_class_value():
    value = "some string"
    assert _is_vault(value) is False
