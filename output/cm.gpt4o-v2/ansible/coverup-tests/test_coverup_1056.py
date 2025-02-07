# file: lib/ansible/parsing/yaml/objects.py:345-346
# asked: {"lines": [345, 346], "branches": []}
# gained: {"lines": [345, 346], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = mock_vault
    return obj

def test_startswith(encrypted_unicode):
    encrypted_unicode._ciphertext = b"decrypted_data"
    assert encrypted_unicode.startswith("decrypted") is True
    assert encrypted_unicode.startswith("data", start=10) is True
    assert encrypted_unicode.startswith("data", start=0, end=9) is False
