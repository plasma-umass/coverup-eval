# file: lib/ansible/parsing/yaml/objects.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isascii(self):
        return True

@pytest.fixture
def mock_data():
    return MockData()

def test_isascii(monkeypatch, mock_data):
    def mock_init(self, data):
        self._data = data
        self.vault = True

    def mock_data_property(self):
        return self._data

    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, '__init__', mock_init)
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_data_property))
    
    obj = AnsibleVaultEncryptedUnicode(mock_data)
    assert obj.isascii() == True
