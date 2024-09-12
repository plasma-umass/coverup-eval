# file: lib/ansible/parsing/yaml/objects.py:201-206
# asked: {"lines": [201, 202, 203, 204, 205, 206], "branches": [[202, 203], [202, 204], [204, 205], [204, 206]]}
# gained: {"lines": [201, 202, 203, 204, 205, 206], "branches": [[202, 203], [202, 204], [204, 205], [204, 206]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils.six import text_type

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_" + ciphertext.decode()

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = MockVault()
    return obj

def test_add_same_type(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode(b"other_ciphertext")
    other.vault = MockVault()
    result = encrypted_unicode + other
    assert result == "decrypted_ciphertext" + "decrypted_other_ciphertext"

def test_add_text_type(encrypted_unicode):
    other = text_type("some_text")
    result = encrypted_unicode + other
    assert result == "decrypted_ciphertext" + "some_text"

def test_add_other_type(encrypted_unicode):
    other = b"other_bytes"
    result = encrypted_unicode + other
    assert result == "decrypted_ciphertext" + "other_bytes"
