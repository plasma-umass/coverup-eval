# file: lib/ansible/parsing/yaml/objects.py:185-188
# asked: {"lines": [185, 186, 187, 188], "branches": [[186, 187], [186, 188]]}
# gained: {"lines": [185, 186, 187, 188], "branches": [[186, 187], [186, 188]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_contains_with_same_class(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode("ciphertext")
    other.vault = MockVault()
    assert other in encrypted_unicode

def test_contains_with_string(encrypted_unicode):
    assert "decrypted_data" in encrypted_unicode
