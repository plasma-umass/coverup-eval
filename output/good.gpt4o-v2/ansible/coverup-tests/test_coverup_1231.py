# file: lib/ansible/parsing/yaml/objects.py:319-322
# asked: {"lines": [320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [320, 321, 322], "branches": [[320, 321], [320, 322]]}

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

def test_rfind_with_encrypted_unicode(encrypted_unicode):
    sub_obj = AnsibleVaultEncryptedUnicode("ciphertext")
    sub_obj.vault = MockVault()
    result = encrypted_unicode.rfind(sub_obj)
    assert result == encrypted_unicode.data.rfind(sub_obj.data)

def test_rfind_with_string(encrypted_unicode):
    result = encrypted_unicode.rfind("data")
    assert result == encrypted_unicode.data.rfind("data")
