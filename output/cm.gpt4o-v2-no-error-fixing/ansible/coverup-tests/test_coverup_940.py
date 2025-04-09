# file: lib/ansible/parsing/yaml/objects.py:268-269
# asked: {"lines": [269], "branches": []}
# gained: {"lines": [269], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "12345"

@pytest.fixture
def encrypted_unicode():
    ciphertext = b'$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70'
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_isdecimal(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', '12345')
    assert encrypted_unicode.isdecimal() == True

    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', '12345a')
    assert encrypted_unicode.isdecimal() == False
