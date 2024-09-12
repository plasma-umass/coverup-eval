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
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_le_with_same_type(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode("other_ciphertext")
    other.vault = MockVault()
    assert (encrypted_unicode <= other) == (encrypted_unicode.data <= other.data)

def test_le_with_string(encrypted_unicode):
    assert (encrypted_unicode <= "some_string") == (encrypted_unicode.data <= "some_string")
