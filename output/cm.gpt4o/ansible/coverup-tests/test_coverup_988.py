# file lib/ansible/parsing/yaml/objects.py:283-284
# lines [283, 284]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isprintable(self):
        return True

@pytest.fixture
def mock_data():
    return MockData()

def test_ansible_vault_encrypted_unicode_isprintable(mock_data, mocker):
    mocker.patch.object(AnsibleVaultEncryptedUnicode, 'data', mock_data)
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    assert obj.isprintable() == True
