# file lib/ansible/parsing/yaml/objects.py:221-222
# lines [221, 222]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unicode import to_text

class MockSequence:
    def __getitem__(self, index):
        return "mocked"

    def __len__(self):
        return 1

class MockAnsibleBaseYAMLObject:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject, AnsibleVaultEncryptedUnicode):
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self.vault = None

    @property
    def data(self):
        return self.ciphertext

def test_ansible_vault_encrypted_unicode_rmod():
    obj = TestAnsibleVaultEncryptedUnicode("mocked")
    template = "This is a %s test"
    result = template % obj
    assert result == "This is a mocked test"
