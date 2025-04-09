# file lib/ansible/parsing/yaml/objects.py:221-222
# lines [222]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

@pytest.fixture
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_value")

def test_ansible_vault_encrypted_unicode_rmod(mock_ansible_vault_encrypted_unicode):
    template = "The secret is: %s"
    result = mock_ansible_vault_encrypted_unicode.__rmod__(template)
    assert result == "The secret is: encrypted_value"
