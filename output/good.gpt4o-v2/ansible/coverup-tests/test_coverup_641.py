# file: lib/ansible/parsing/yaml/objects.py:124-127
# asked: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}
# gained: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_ne_with_vault(encrypted_unicode, mocker):
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault
    mocker.patch.object(encrypted_unicode.__class__, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    
    assert not (encrypted_unicode != "decrypted_data")
    assert encrypted_unicode != "other_data"

def test_ne_without_vault(encrypted_unicode):
    encrypted_unicode.vault = None
    
    assert encrypted_unicode != "any_data"
