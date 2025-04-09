# file: lib/ansible/parsing/yaml/objects.py:129-132
# asked: {"lines": [129, 132], "branches": []}
# gained: {"lines": [129, 132], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        self.value = value

    def __getitem__(self, index):
        return self.value[index]

    def __len__(self):
        return len(self.value)

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_string")

def test_reversed(mock_vault_unicode, mocker):
    mock_to_text = mocker.patch('ansible.parsing.yaml.objects.to_text', return_value="gnirts_detpyrcne")
    reversed_value = reversed(mock_vault_unicode)
    assert reversed_value == "gnirts_detpyrcne"
    mock_to_text.assert_called_once_with("gnirts_detpyrcne", errors='surrogate_or_strict')
