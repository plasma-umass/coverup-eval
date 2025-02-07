# file: lib/ansible/parsing/yaml/objects.py:221-222
# asked: {"lines": [222], "branches": []}
# gained: {"lines": [222], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def test_rmod():
    template = "Encrypted value: %s"
    encrypted_value = MockAnsibleVaultEncryptedUnicode("secret")
    result = encrypted_value.__rmod__(template)
    assert result == "Encrypted value: secret"
