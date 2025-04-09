# file: lib/ansible/parsing/yaml/objects.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj):
        return ciphertext

@pytest.fixture
def mock_data_numeric():
    return "12345"

@pytest.fixture
def mock_data_non_numeric():
    return "abcde"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_isnumeric_true(mock_data_numeric, mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode(mock_data_numeric)
    monkeypatch.setattr(obj, 'vault', mock_vault)
    assert obj.isnumeric() is True

def test_isnumeric_false(mock_data_non_numeric, mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode(mock_data_non_numeric)
    monkeypatch.setattr(obj, 'vault', mock_vault)
    assert obj.isnumeric() is False
