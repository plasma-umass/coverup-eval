# file: lib/ansible/parsing/yaml/objects.py:234-237
# asked: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_count_with_sub_of_same_type(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    sub_obj = AnsibleVaultEncryptedUnicode("ciphertext")
    sub_obj.vault = MockVault()
    count = encrypted_unicode.count(sub_obj)
    assert count == 1

def test_count_with_sub_of_different_type(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', new_callable=mocker.PropertyMock, return_value="decrypted_data")
    count = encrypted_unicode.count("decrypted_data")
    assert count == 1
