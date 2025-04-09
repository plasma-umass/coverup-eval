# file: lib/ansible/parsing/yaml/objects.py:253-254
# asked: {"lines": [254], "branches": []}
# gained: {"lines": [254], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode()

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("encrypted_text")
    obj.vault = MockVault()
    return obj

def test_format_map(encrypted_unicode):
    encrypted_unicode._ciphertext = b"Hello, {name}!"
    result = encrypted_unicode.format_map({"name": "World"})
    assert result == "Hello, World!"
