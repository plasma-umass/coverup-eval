# file: lib/ansible/parsing/yaml/objects.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(b'some encrypted text')
    obj.vault = mock_vault
    return obj

def test_isprintable(encrypted_unicode):
    encrypted_unicode._ciphertext = b'some decrypted text'
    assert encrypted_unicode.isprintable() == 'some decrypted text'.isprintable()
