# file lib/ansible/parsing/yaml/objects.py:357-358
# lines [358]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def translate(self, *args):
        return "translated"

@pytest.fixture
def mock_data():
    return MockData()

def test_ansible_vault_encrypted_unicode_translate(mock_data, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', mock_data)
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    result = obj.translate("arg1", "arg2")
    assert result == "translated"
