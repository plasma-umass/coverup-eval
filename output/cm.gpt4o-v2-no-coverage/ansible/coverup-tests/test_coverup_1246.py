# file: lib/ansible/parsing/yaml/objects.py:242-243
# asked: {"lines": [243], "branches": []}
# gained: {"lines": [243], "branches": []}

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
    obj = AnsibleVaultEncryptedUnicode(b"line1\tline2")
    obj.vault = mock_vault
    return obj

def test_expandtabs(encrypted_unicode):
    result = encrypted_unicode.expandtabs(4)
    assert result == "line1   line2"
