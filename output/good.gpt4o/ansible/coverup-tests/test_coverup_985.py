# file lib/ansible/parsing/yaml/objects.py:265-266
# lines [265, 266]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isascii(self):
        return True

@pytest.fixture
def mock_data():
    return MockData()

def test_ansible_vault_encrypted_unicode_isascii(mock_data, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', mock_data)
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    assert obj.isascii() == True
