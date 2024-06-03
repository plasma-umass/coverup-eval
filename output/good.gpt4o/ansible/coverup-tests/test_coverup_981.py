# file lib/ansible/parsing/yaml/objects.py:259-260
# lines [259, 260]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isalpha(self):
        return True

@pytest.fixture
def mock_data(mocker):
    return mocker.patch('ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode.data', new_callable=mocker.PropertyMock, return_value=MockData())

def test_ansible_vault_encrypted_unicode_isalpha(mock_data):
    obj = AnsibleVaultEncryptedUnicode(ciphertext='dummy_ciphertext')
    assert obj.isalpha() == True
