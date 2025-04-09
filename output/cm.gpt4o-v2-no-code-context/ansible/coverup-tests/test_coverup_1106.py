# file: lib/ansible/parsing/yaml/objects.py:221-222
# asked: {"lines": [222], "branches": []}
# gained: {"lines": [222], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def test_ansible_vault_encrypted_unicode_rmod():
    mock_obj = MockAnsibleVaultEncryptedUnicode("encrypted_value")
    template = "The value is: %s"
    result = template % mock_obj
    assert result == "The value is: encrypted_value"

    # Ensure the __rmod__ method is called
    result_rmod = mock_obj.__rmod__(template)
    assert result_rmod == "The value is: encrypted_value"
