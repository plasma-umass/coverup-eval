# file: lib/ansible/module_utils/common/json.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest

# Assuming the _is_vault function is part of a module named 'json_utils'
from ansible.module_utils.common.json import _is_vault

def test_is_vault_with_encrypted_attribute():
    class EncryptedObject:
        __ENCRYPTED__ = True

    obj = EncryptedObject()
    assert _is_vault(obj) is True

def test_is_vault_without_encrypted_attribute():
    class NonEncryptedObject:
        pass

    obj = NonEncryptedObject()
    assert _is_vault(obj) is False

def test_is_vault_with_encrypted_attribute_false():
    class EncryptedObjectFalse:
        __ENCRYPTED__ = False

    obj = EncryptedObjectFalse()
    assert _is_vault(obj) is False
