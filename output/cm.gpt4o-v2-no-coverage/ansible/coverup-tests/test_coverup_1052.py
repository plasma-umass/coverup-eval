# file: lib/ansible/parsing/yaml/objects.py:304-305
# asked: {"lines": [304, 305], "branches": []}
# gained: {"lines": [304, 305], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("encrypted_data")
    obj.vault = MockVault()
    return obj

def test_lstrip_no_chars(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="   decrypted_data")
    result = encrypted_unicode.lstrip()
    assert result == "decrypted_data".lstrip()

def test_lstrip_with_chars(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="xxxdecrypted_data")
    result = encrypted_unicode.lstrip('x')
    assert result == "decrypted_data".lstrip('x')
