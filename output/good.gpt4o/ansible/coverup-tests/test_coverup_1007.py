# file lib/ansible/parsing/yaml/objects.py:304-305
# lines [304, 305]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def __init__(self, data):
        self.data = data

    def lstrip(self, chars=None):
        return self.data.lstrip(chars)

@pytest.fixture
def mock_data():
    return MockData("   encrypted data")

@pytest.fixture
def ansible_vault_encrypted_unicode(mock_data, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', mock_data)
    return AnsibleVaultEncryptedUnicode(ciphertext="dummy ciphertext")

def test_lstrip_no_chars(ansible_vault_encrypted_unicode):
    result = ansible_vault_encrypted_unicode.lstrip()
    assert result == "encrypted data"

def test_lstrip_with_chars(ansible_vault_encrypted_unicode):
    result = ansible_vault_encrypted_unicode.lstrip(" e")
    assert result == "ncrypted data"
