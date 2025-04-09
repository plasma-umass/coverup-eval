# file lib/ansible/parsing/yaml/objects.py:256-257
# lines [256, 257]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_index():
    # Create a mock object with sample data
    mock_data = "encrypted_string"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    # Test the index method
    assert obj.index("encrypted") == 0
    assert obj.index("string") == 10
    
    # Test with start and end parameters
    assert obj.index("string", 5) == 10
    assert obj.index("encrypted", 0, 9) == 0
    
    # Test for a substring that does not exist
    with pytest.raises(ValueError):
        obj.index("not_in_string")

    # Test for a substring with start and end that does not exist
    with pytest.raises(ValueError):
        obj.index("encrypted", 1, 9)
