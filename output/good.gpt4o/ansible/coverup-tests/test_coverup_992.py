# file lib/ansible/parsing/yaml/objects.py:274-275
# lines [274, 275]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockSequence:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

class MockAnsibleBaseYAMLObject:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject, AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        super().__init__(data)
        self.vault = True

@pytest.fixture
def mock_data():
    return "valid_identifier"

@pytest.fixture
def invalid_mock_data():
    return "123invalid"

def test_isidentifier(mock_data):
    obj = TestAnsibleVaultEncryptedUnicode(mock_data)
    assert obj.isidentifier() == True

def test_isidentifier_invalid(invalid_mock_data):
    obj = TestAnsibleVaultEncryptedUnicode(invalid_mock_data)
    assert obj.isidentifier() == False
