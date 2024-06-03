# file lib/ansible/parsing/yaml/objects.py:112-114
# lines [112, 113, 114]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_ansible_vault_encrypted_unicode_data_setter():
    class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self):
            self._ciphertext = None

    obj = MockAnsibleVaultEncryptedUnicode()
    test_value = "test_value"
    obj.data = test_value

    assert obj._ciphertext == to_bytes(test_value)
