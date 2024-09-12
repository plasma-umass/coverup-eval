# file: lib/ansible/parsing/yaml/objects.py:137-138
# asked: {"lines": [137, 138], "branches": []}
# gained: {"lines": [137, 138], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = MockVault()
    return obj

def test_unicode_method(encrypted_unicode):
    result = encrypted_unicode.__unicode__()
    assert result == to_text("decrypted_text", errors='surrogate_or_strict')
