# file lib/ansible/parsing/yaml/objects.py:268-269
# lines [268, 269]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockSequence:
    def __init__(self, data):
        self.data = data

class MockAnsibleBaseYAMLObject:
    pass

class TestAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode, MockSequence, MockAnsibleBaseYAMLObject):
    def __init__(self, data):
        MockSequence.__init__(self, data)
        MockAnsibleBaseYAMLObject.__init__(self)
        self.vault = None  # Mocking the vault attribute

@pytest.fixture
def mock_data():
    return "12345"

@pytest.fixture
def mock_object(mock_data):
    return TestAnsibleVaultEncryptedUnicode(mock_data)

def test_isdecimal(mock_object):
    assert mock_object.isdecimal() == True

@pytest.fixture
def mock_non_decimal_data():
    return "abcde"

@pytest.fixture
def mock_non_decimal_object(mock_non_decimal_data):
    return TestAnsibleVaultEncryptedUnicode(mock_non_decimal_data)

def test_isdecimal_non_decimal(mock_non_decimal_object):
    assert mock_non_decimal_object.isdecimal() == False
