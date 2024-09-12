# file: lib/ansible/parsing/yaml/objects.py:119-122
# asked: {"lines": [119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_eq_with_vault(encrypted_unicode, mocker):
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault
    mocker.patch.object(encrypted_unicode.__class__, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    
    assert encrypted_unicode == "decrypted_data"

def test_eq_without_vault(encrypted_unicode):
    encrypted_unicode.vault = None
    
    assert not (encrypted_unicode == "any_data")
