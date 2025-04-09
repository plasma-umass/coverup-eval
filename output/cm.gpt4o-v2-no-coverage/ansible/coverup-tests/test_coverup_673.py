# file: lib/ansible/parsing/yaml/objects.py:245-248
# asked: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}
# gained: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def encrypted_unicode():
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_find_with_substring(encrypted_unicode):
    encrypted_unicode._ciphertext = b"this is some encrypted_data"
    assert encrypted_unicode.find("some") == 8

def test_find_with_ansible_vault_encrypted_unicode(encrypted_unicode):
    encrypted_unicode._ciphertext = b"this is some encrypted_data"
    sub = AnsibleVaultEncryptedUnicode(b"some")
    sub.vault = MockVault()
    assert encrypted_unicode.find(sub) == 8

def test_find_with_start_and_end(encrypted_unicode):
    encrypted_unicode._ciphertext = b"this is some encrypted_data"
    assert encrypted_unicode.find("some", 5, 15) == 8

def test_find_not_found(encrypted_unicode):
    encrypted_unicode._ciphertext = b"this is some encrypted_data"
    assert encrypted_unicode.find("notfound") == -1
