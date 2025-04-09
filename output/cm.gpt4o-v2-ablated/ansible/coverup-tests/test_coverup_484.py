# file: lib/ansible/module_utils/common/json.py:22-23
# asked: {"lines": [23], "branches": []}
# gained: {"lines": [23], "branches": []}

import pytest

from ansible.module_utils.common.json import _is_vault

def test_is_vault_with_encrypted_attribute():
    class Encrypted:
        __ENCRYPTED__ = True

    encrypted_instance = Encrypted()
    assert _is_vault(encrypted_instance) is True

def test_is_vault_without_encrypted_attribute():
    class NotEncrypted:
        pass

    not_encrypted_instance = NotEncrypted()
    assert _is_vault(not_encrypted_instance) is False

def test_is_vault_with_encrypted_attribute_false():
    class EncryptedFalse:
        __ENCRYPTED__ = False

    encrypted_false_instance = EncryptedFalse()
    assert _is_vault(encrypted_false_instance) is False

def test_is_vault_with_non_class_object():
    non_class_object = {'__ENCRYPTED__': True}
    assert _is_vault(non_class_object) is False
