# file: lib/ansible/parsing/yaml/objects.py:292-293
# asked: {"lines": [292, 293], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def encrypted_unicode():
    ciphertext = b"ENCRYPTEDDATA"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_isupper(encrypted_unicode):
    encrypted_unicode._ciphertext = b"ENCRYPTEDDATA"
    assert encrypted_unicode.isupper() == encrypted_unicode.data.isupper()

def test_isupper_false(encrypted_unicode):
    encrypted_unicode._ciphertext = b"encrypteddata"
    assert encrypted_unicode.isupper() == encrypted_unicode.data.isupper()
