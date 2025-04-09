# file: lib/ansible/parsing/yaml/objects.py:124-127
# asked: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}
# gained: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self.data = data

    def decrypt(self, ciphertext, obj=None):
        return self.data

@pytest.fixture
def mock_vault():
    return MockVault(data="mock_data")

def test_ansible_vault_encrypted_unicode_ne_with_vault(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(ciphertext="mock_ciphertext")
    obj.vault = mock_vault
    
    assert obj != "different_data"
    assert not (obj != "mock_data")

def test_ansible_vault_encrypted_unicode_ne_without_vault():
    obj = AnsibleVaultEncryptedUnicode(ciphertext="mock_ciphertext")
    obj.vault = None
    
    assert obj != "any_data"
