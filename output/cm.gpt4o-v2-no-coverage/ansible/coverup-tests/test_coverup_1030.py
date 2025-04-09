# file: lib/ansible/parsing/yaml/objects.py:268-269
# asked: {"lines": [268, 269], "branches": []}
# gained: {"lines": [268, 269], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockData:
    def isdecimal(self):
        return True

@pytest.fixture
def mock_data(monkeypatch):
    mock_data_instance = MockData()
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', mock_data_instance)
    return mock_data_instance

def test_isdecimal(mock_data):
    encrypted_unicode = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    assert encrypted_unicode.isdecimal() == True
