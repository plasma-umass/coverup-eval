# file: lib/ansible/parsing/yaml/objects.py:170-173
# asked: {"lines": [170, 171, 172, 173], "branches": [[171, 172], [171, 173]]}
# gained: {"lines": [170, 171, 172, 173], "branches": [[171, 172], [171, 173]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("encrypted_data")

def test_le_with_same_class(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode("other_encrypted_data")
    other.vault = MockVault()
    encrypted_unicode.vault = MockVault()
    assert encrypted_unicode <= other

def test_le_with_string(encrypted_unicode):
    encrypted_unicode.vault = MockVault()
    assert encrypted_unicode <= "decrypted_data"

def test_le_with_different_class(encrypted_unicode):
    class DifferentClass:
        data = "decrypted_data"
    other = DifferentClass()
    encrypted_unicode.vault = MockVault()
    assert encrypted_unicode <= other.data
