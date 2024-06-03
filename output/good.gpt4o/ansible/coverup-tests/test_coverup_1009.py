# file lib/ansible/parsing/yaml/objects.py:357-358
# lines [357, 358]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleBaseYAMLObject:
    def __init__(self, data):
        self.data = data

class MockSequence:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject):
    def translate(self, *args):
        return self.data.translate(*args)

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(mocker):
    mock_data = mocker.Mock()
    mock_data.translate.return_value = "translated_data"
    return TestAnsibleVaultEncryptedUnicode(mock_data)

def test_translate(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.translate("arg1", "arg2")
    mock_ansible_vault_encrypted_unicode.data.translate.assert_called_once_with("arg1", "arg2")
    assert result == "translated_data"
