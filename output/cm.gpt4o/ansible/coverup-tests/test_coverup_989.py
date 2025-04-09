# file lib/ansible/parsing/yaml/objects.py:289-290
# lines [289, 290]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def istitle(self):
        return True

@pytest.fixture
def mock_data(mocker):
    return mocker.patch('ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode.data', new_callable=mocker.PropertyMock, return_value=MockData())

def test_ansible_vault_encrypted_unicode_istitle(mock_data):
    obj = AnsibleVaultEncryptedUnicode(ciphertext='dummy_ciphertext')
    assert obj.istitle() == True
