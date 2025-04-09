# file: lib/ansible/parsing/yaml/objects.py:351-352
# asked: {"lines": [351, 352], "branches": []}
# gained: {"lines": [351, 352], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode().swapcase()

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode(b"encrypted_data")

def test_swapcase(encrypted_unicode, mocker):
    mock_vault = MockVault()
    mocker.patch.object(encrypted_unicode, 'vault', mock_vault)
    encrypted_unicode.vault = mock_vault
    assert encrypted_unicode.swapcase() == "ENCRYPTED_DATA".swapcase()
