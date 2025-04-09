# file: lib/ansible/parsing/yaml/objects.py:234-237
# asked: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}

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

def test_count_with_string(encrypted_unicode):
    encrypted_unicode.data = "decrypted_data"
    assert encrypted_unicode.count("data") == 1

def test_count_with_ansible_vault_encrypted_unicode(encrypted_unicode):
    sub_obj = AnsibleVaultEncryptedUnicode("ciphertext")
    sub_obj.vault = MockVault()
    sub_obj.data = "data"
    encrypted_unicode.data = "decrypted_data"
    assert encrypted_unicode.count(sub_obj) == 1
