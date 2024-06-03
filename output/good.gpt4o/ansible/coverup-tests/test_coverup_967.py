# file lib/ansible/parsing/yaml/objects.py:262-263
# lines [262, 263]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleBaseYAMLObject:
    def __init__(self, data):
        self.data = data

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(mocker):
    mocker.patch('ansible.parsing.yaml.objects.AnsibleBaseYAMLObject', MockAnsibleBaseYAMLObject)
    return AnsibleVaultEncryptedUnicode("mockdata123")

def test_isalnum(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.isalnum() == True

def test_isalnum_non_alnum(mocker):
    mocker.patch('ansible.parsing.yaml.objects.AnsibleBaseYAMLObject', MockAnsibleBaseYAMLObject)
    obj = AnsibleVaultEncryptedUnicode("mock data!")
    assert obj.isalnum() == False
