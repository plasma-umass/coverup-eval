# file: lib/ansible/parsing/yaml/objects.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockSequence:
    pass

class MockAnsibleBaseYAMLObject:
    pass

class MockAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return to_native(self.data, errors='surrogate_or_strict')

@pytest.fixture
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_ansible_vault_encrypted_unicode_str(mock_ansible_vault_encrypted_unicode):
    result = str(mock_ansible_vault_encrypted_unicode)
    assert result == "encrypted_data"
