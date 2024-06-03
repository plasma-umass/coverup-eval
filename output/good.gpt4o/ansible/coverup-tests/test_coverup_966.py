# file lib/ansible/parsing/yaml/objects.py:134-135
# lines [134, 135]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_str():
    mock_data = b'\x80\x81\x82'
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    result = str(obj)
    assert result == to_native(mock_data, errors='surrogate_or_strict')
