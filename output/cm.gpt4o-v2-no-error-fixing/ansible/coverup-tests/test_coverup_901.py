# file: lib/ansible/parsing/yaml/objects.py:234-237
# asked: {"lines": [235, 236, 237], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [235, 236, 237], "branches": [[235, 236], [235, 237]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("encrypted_data")

def test_count_with_subclass(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', "decrypted_data")
    sub_instance = AnsibleVaultEncryptedUnicode("sub_encrypted_data")
    mocker.patch.object(sub_instance, 'data', "sub_decrypted_data")
    
    result = encrypted_unicode.count(sub_instance)
    
    assert result == "decrypted_data".count("sub_decrypted_data")

def test_count_with_string(encrypted_unicode, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', "decrypted_data")
    
    result = encrypted_unicode.count("sub_decrypted_data")
    
    assert result == "decrypted_data".count("sub_decrypted_data")
