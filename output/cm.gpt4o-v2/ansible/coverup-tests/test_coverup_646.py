# file: lib/ansible/parsing/yaml/objects.py:245-248
# asked: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}
# gained: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}

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

def test_find_with_string(encrypted_unicode):
    encrypted_unicode._ciphertext = b"decrypted_data"
    result = encrypted_unicode.find("data")
    assert result == 10

def test_find_with_ansible_vault_encrypted_unicode(encrypted_unicode):
    encrypted_unicode._ciphertext = b"decrypted_data"
    sub_obj = AnsibleVaultEncryptedUnicode("ciphertext")
    sub_obj.vault = MockVault()
    sub_obj._ciphertext = b"decrypted_data"
    result = encrypted_unicode.find(sub_obj)
    assert result == 0
