# file: lib/ansible/parsing/yaml/objects.py:185-188
# asked: {"lines": [186, 187, 188], "branches": [[186, 187], [186, 188]]}
# gained: {"lines": [186, 187, 188], "branches": [[186, 187], [186, 188]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    vault = MockVault()
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = vault
    return obj

def test_contains_with_same_type(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    other = AnsibleVaultEncryptedUnicode("other_ciphertext")
    other.vault = encrypted_unicode.vault
    assert other in encrypted_unicode

def test_contains_with_string(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    assert "decrypted_data" in encrypted_unicode
