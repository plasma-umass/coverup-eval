# file: lib/ansible/parsing/yaml/objects.py:250-251
# asked: {"lines": [250, 251], "branches": []}
# gained: {"lines": [250], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleBaseYAMLObject:
    pass

class MockSequence:
    pass

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(monkeypatch):
    class MockAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject):
        def __init__(self, data):
            self.data = data

        def format(self, *args, **kwds):
            return self.data.format(*args, **kwds)

    monkeypatch.setattr('ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode', MockAnsibleVaultEncryptedUnicode)
    return MockAnsibleVaultEncryptedUnicode

def test_format(mock_ansible_vault_encrypted_unicode):
    instance = mock_ansible_vault_encrypted_unicode("Hello, {}!")
    formatted = instance.format("World")
    assert formatted == "Hello, World!"
