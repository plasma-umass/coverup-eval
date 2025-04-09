# file: lib/ansible/parsing/yaml/objects.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "   " if ciphertext == b"ciphertext" else "text"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_isspace(encrypted_unicode, mocker):
    mocker.patch.object(encrypted_unicode, 'vault', MockVault())
    assert encrypted_unicode.isspace() == True

    mocker.patch.object(encrypted_unicode, '_ciphertext', b"other_ciphertext")
    assert encrypted_unicode.isspace() == False
