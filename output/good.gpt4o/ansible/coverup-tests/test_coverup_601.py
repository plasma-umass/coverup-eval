# file lib/ansible/parsing/yaml/objects.py:124-127
# lines [124, 125, 126, 127]
# branches ['125->126', '125->127']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self.data = data

    def decrypt(self, ciphertext, obj=None):
        return self.data

@pytest.fixture
def mock_vault():
    return MockVault("decrypted_data")

@pytest.fixture
def ansible_vault_encrypted_unicode(mock_vault):
    class TestAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self, vault):
            self.vault = vault
            self._ciphertext = "encrypted_data"

    return TestAnsibleVaultEncryptedUnicode(mock_vault)

def test_ansible_vault_encrypted_unicode_ne_with_vault(ansible_vault_encrypted_unicode):
    assert ansible_vault_encrypted_unicode != "some_other_data"
    assert not (ansible_vault_encrypted_unicode != "decrypted_data")

def test_ansible_vault_encrypted_unicode_ne_without_vault():
    class TestAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self):
            self.vault = None
            self._ciphertext = "encrypted_data"

    obj = TestAnsibleVaultEncryptedUnicode()
    assert obj != "any_data"
