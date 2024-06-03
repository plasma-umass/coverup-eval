# file lib/ansible/parsing/yaml/objects.py:309-310
# lines [309, 310]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock attribute to bypass the vault check

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_partition():
    # Create a mock object with sample data
    mock_data = "vaulted_data"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    # Test the partition method
    sep = "_"
    result = obj.partition(sep)
    
    # Verify the result
    assert result == ("vaulted", "_", "data")

    # Clean up
    del obj
