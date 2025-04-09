# file: lib/ansible/parsing/yaml/objects.py:250-251
# asked: {"lines": [250, 251], "branches": []}
# gained: {"lines": [250, 251], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = MockVault()
    return obj

def test_format(encrypted_unicode):
    result = encrypted_unicode.format()
    assert result == "decrypted_text"

def test_format_with_args(encrypted_unicode, mocker):
    mocker.patch.object(MockVault, 'decrypt', return_value="Hello, {}!")
    result = encrypted_unicode.format("World")
    assert result == "Hello, World!"

def test_format_with_kwargs(encrypted_unicode, mocker):
    mocker.patch.object(MockVault, 'decrypt', return_value="Hello, {name}!")
    result = encrypted_unicode.format(name="World")
    assert result == "Hello, World!"
