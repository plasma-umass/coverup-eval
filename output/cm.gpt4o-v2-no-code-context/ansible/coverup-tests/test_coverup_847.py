# file: lib/ansible/module_utils/common/json.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest

from ansible.module_utils.common.json import _is_vault

def test_is_vault_with_encrypted_attribute():
    class EncryptedValue:
        __ENCRYPTED__ = True

    value = EncryptedValue()
    assert _is_vault(value) is True

def test_is_vault_without_encrypted_attribute():
    class NonEncryptedValue:
        pass

    value = NonEncryptedValue()
    assert _is_vault(value) is False

def test_is_vault_with_encrypted_attribute_false():
    class EncryptedValueFalse:
        __ENCRYPTED__ = False

    value = EncryptedValueFalse()
    assert _is_vault(value) is False
