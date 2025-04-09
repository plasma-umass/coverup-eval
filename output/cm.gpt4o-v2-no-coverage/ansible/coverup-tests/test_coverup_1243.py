# file: lib/ansible/parsing/yaml/objects.py:259-260
# asked: {"lines": [260], "branches": []}
# gained: {"lines": [260], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isalpha(self):
        return True

@pytest.fixture
def mock_data(monkeypatch):
    mock_data_instance = MockData()
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', mock_data_instance)
    return mock_data_instance

def test_isalpha(mock_data):
    encrypted_unicode = AnsibleVaultEncryptedUnicode(ciphertext="ciphertext")
    assert encrypted_unicode.isalpha() == True
