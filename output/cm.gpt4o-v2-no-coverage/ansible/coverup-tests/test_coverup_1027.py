# file: lib/ansible/parsing/yaml/objects.py:158-159
# asked: {"lines": [158, 159], "branches": []}
# gained: {"lines": [158, 159], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_hash(encrypted_unicode, mocker):
    mocker.patch.object(encrypted_unicode, 'vault', MockVault())
    assert hash(encrypted_unicode) == hash("decrypted_data")
