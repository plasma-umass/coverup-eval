# file lib/ansible/parsing/yaml/objects.py:140-141
# lines [140, 141]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

class MockAnsibleBaseYAMLObject:
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

class MockSequence:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject, AnsibleVaultEncryptedUnicode):
    pass

@pytest.fixture
def mock_data():
    return "mock_encrypted_data"

def test_encode(mock_data):
    obj = TestAnsibleVaultEncryptedUnicode(mock_data)
    encoded_data = obj.encode(encoding='utf-8', errors='strict')
    assert encoded_data == to_bytes(mock_data, encoding='utf-8', errors='strict')
