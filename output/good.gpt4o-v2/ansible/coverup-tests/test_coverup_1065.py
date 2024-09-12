# file: lib/ansible/parsing/yaml/objects.py:253-254
# asked: {"lines": [253, 254], "branches": []}
# gained: {"lines": [253, 254], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "This is a {key}"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_format_map(encrypted_unicode):
    mapping = {"key": "value"}
    result = encrypted_unicode.format_map(mapping)
    assert result == "This is a value"
