# file lib/ansible/parsing/yaml/objects.py:295-296
# lines [295, 296]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_join():
    # Create a mock object with some data
    mock_obj = MockAnsibleVaultEncryptedUnicode("secret")

    # Test the join method
    result = mock_obj.join(["a", "b", "c"])
    
    # Assert the expected result
    assert result == "asecretbsecretc"

    # Clean up if necessary (not needed in this simple case)
