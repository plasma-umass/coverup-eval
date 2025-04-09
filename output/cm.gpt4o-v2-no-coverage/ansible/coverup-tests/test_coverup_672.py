# file: lib/ansible/parsing/yaml/objects.py:165-168
# asked: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}
# gained: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode(b"encrypted_text")

def test_lt_with_same_class(encrypted_unicode, mocker):
    mock_vault = MockVault()
    mocker.patch.object(encrypted_unicode, 'vault', mock_vault)
    other = AnsibleVaultEncryptedUnicode(b"other_encrypted_text")
    mocker.patch.object(other, 'vault', mock_vault)
    
    assert (encrypted_unicode < other) == ("decrypted_text" < "decrypted_text")

def test_lt_with_string(encrypted_unicode, mocker):
    mock_vault = MockVault()
    mocker.patch.object(encrypted_unicode, 'vault', mock_vault)
    
    assert (encrypted_unicode < "some_string") == ("decrypted_text" < "some_string")
