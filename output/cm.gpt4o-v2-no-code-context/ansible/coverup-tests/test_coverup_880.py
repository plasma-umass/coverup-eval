# file: lib/ansible/parsing/yaml/objects.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def __init__(self, value):
        self.value = value

    def isnumeric(self):
        return self.value.isnumeric()

@pytest.fixture
def mock_ansible_vault_encrypted_unicode(monkeypatch):
    def mock_init(self, data):
        self._data = data
        self.vault = True

    def mock_data(self):
        return self._data

    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "__init__", mock_init)
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "data", property(mock_data))

def test_isnumeric_true(mock_ansible_vault_encrypted_unicode):
    obj = AnsibleVaultEncryptedUnicode(MockData("12345"))
    assert obj.isnumeric() is True

def test_isnumeric_false(mock_ansible_vault_encrypted_unicode):
    obj = AnsibleVaultEncryptedUnicode(MockData("abcde"))
    assert obj.isnumeric() is False
