# file lib/ansible/parsing/yaml/objects.py:129-132
# lines [129, 132]
# branches []

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
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_string")

def test_reversed_method(mock_ansible_vault_encrypted_unicode):
    reversed_value = mock_ansible_vault_encrypted_unicode.__reversed__()
    expected_value = to_text("encrypted_string"[::-1], errors='surrogate_or_strict')
    assert reversed_value == expected_value
