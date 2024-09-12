# file: lib/ansible/parsing/yaml/objects.py:250-251
# asked: {"lines": [250, 251], "branches": []}
# gained: {"lines": [250, 251], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "Hello, {}!"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = mock_vault
    return obj

def test_format_method(encrypted_unicode):
    formatted = encrypted_unicode.format("World")
    assert formatted == "Hello, World!"
