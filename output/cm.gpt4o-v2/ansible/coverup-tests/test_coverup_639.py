# file: lib/ansible/parsing/yaml/objects.py:208-211
# asked: {"lines": [208, 209, 210, 211], "branches": [[209, 210], [209, 211]]}
# gained: {"lines": [208, 209, 210, 211], "branches": [[209, 210], [209, 211]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils.six import text_type
from ansible.module_utils._text import to_text

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = MockVault()
    return obj

def test_radd_with_text_type(encrypted_unicode):
    result = "prefix_" + encrypted_unicode
    assert result == "prefix_decrypted_text"

def test_radd_with_non_text_type(encrypted_unicode):
    result = b"prefix_" + encrypted_unicode
    assert result == "prefix_decrypted_text"
