# file: lib/ansible/parsing/yaml/objects.py:333-334
# asked: {"lines": [333, 334], "branches": []}
# gained: {"lines": [333, 334], "branches": []}

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

def test_rstrip_no_chars(encrypted_unicode):
    encrypted_unicode._ciphertext = b"decrypted_data   "
    result = encrypted_unicode.rstrip()
    assert result == "decrypted_data"

def test_rstrip_with_chars(encrypted_unicode):
    encrypted_unicode._ciphertext = b"decrypted_data!!!"
    result = encrypted_unicode.rstrip("!")
    assert result == "decrypted_data"
