# file lib/ansible/parsing/yaml/objects.py:208-211
# lines [208, 209, 210, 211]
# branches ['209->210', '209->211']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text
from collections.abc import Sequence

class MockAnsibleBaseYAMLObject:
    pass

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode, MockAnsibleBaseYAMLObject):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_radd_with_text_type():
    instance = MockAnsibleVaultEncryptedUnicode("encrypted_data")
    result = "plain_text" + instance
    assert result == "plain_textencrypted_data"

def test_ansible_vault_encrypted_unicode_radd_with_other_type():
    instance = MockAnsibleVaultEncryptedUnicode("encrypted_data")
    result = 123 + instance
    assert result == "123encrypted_data"
