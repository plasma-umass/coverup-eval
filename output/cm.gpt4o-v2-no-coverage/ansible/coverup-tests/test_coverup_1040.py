# file: lib/ansible/parsing/yaml/objects.py:231-232
# asked: {"lines": [231, 232], "branches": []}
# gained: {"lines": [231, 232], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_center(encrypted_unicode, mocker):
    mocker.patch.object(type(encrypted_unicode), 'data', new_callable=mocker.PropertyMock, return_value="decrypted_text")
    centered_text = encrypted_unicode.center(20)
    assert centered_text == "   decrypted_text   "
