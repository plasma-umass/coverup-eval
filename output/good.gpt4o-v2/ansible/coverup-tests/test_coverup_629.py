# file: lib/ansible/parsing/yaml/objects.py:180-183
# asked: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}
# gained: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}

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

def test_ge_with_same_class(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode("other_ciphertext")
    other.vault = MockVault()
    assert encrypted_unicode >= other

def test_ge_with_string(encrypted_unicode):
    assert encrypted_unicode >= "decrypted_data"
