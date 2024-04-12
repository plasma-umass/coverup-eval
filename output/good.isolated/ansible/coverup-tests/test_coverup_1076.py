# file lib/ansible/parsing/yaml/objects.py:116-117
# lines [116, 117]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def is_encrypted(self, data):
        return True

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_is_encrypted(mock_vault):
    ciphertext = "encrypted_data"
    av = AnsibleVaultEncryptedUnicode(ciphertext)
    av.vault = mock_vault
    
    assert av.is_encrypted() == True

    av.vault = None
    assert not av.is_encrypted()

