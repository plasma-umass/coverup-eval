# file: lib/ansible/parsing/yaml/objects.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isprintable(self):
        return True

@pytest.fixture
def mock_data(monkeypatch):
    mock_data_instance = MockData()
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', mock_data_instance)
    return mock_data_instance

def test_isprintable(mock_data):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")
    assert encrypted_unicode.isprintable() == True
