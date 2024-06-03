# file lib/ansible/parsing/yaml/objects.py:292-293
# lines [292, 293]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_isupper():
    mock_data_upper = MockAnsibleVaultEncryptedUnicode("ENCRYPTEDDATA")
    assert mock_data_upper.isupper() == True

    mock_data_lower = MockAnsibleVaultEncryptedUnicode("encrypteddata")
    assert mock_data_lower.isupper() == False

    mock_data_mixed = MockAnsibleVaultEncryptedUnicode("EncryptedData")
    assert mock_data_mixed.isupper() == False
