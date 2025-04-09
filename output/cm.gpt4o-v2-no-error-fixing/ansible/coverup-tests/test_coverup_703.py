# file: lib/ansible/parsing/yaml/objects.py:221-222
# asked: {"lines": [221, 222], "branches": []}
# gained: {"lines": [221], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def test_ansible_vault_encrypted_unicode_rmod():
    template = "Encrypted value: %s"
    encrypted_value = MockAnsibleVaultEncryptedUnicode("secret")
    
    result = template % encrypted_value
    
    assert result == "Encrypted value: secret"
