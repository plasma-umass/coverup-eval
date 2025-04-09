# file: lib/ansible/parsing/yaml/objects.py:319-322
# asked: {"lines": [320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [320, 321, 322], "branches": [[320, 321], [320, 322]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"this is some encrypted data")
    obj.vault = MockVault()
    return obj

def test_rfind_with_string(encrypted_unicode):
    assert encrypted_unicode.rfind("encrypted") == 13

def test_rfind_with_ansible_vault_encrypted_unicode(encrypted_unicode):
    sub_obj = AnsibleVaultEncryptedUnicode(b"encrypted")
    sub_obj.vault = MockVault()
    assert encrypted_unicode.rfind(sub_obj) == 13

def test_rfind_not_found(encrypted_unicode):
    assert encrypted_unicode.rfind("missing") == -1
