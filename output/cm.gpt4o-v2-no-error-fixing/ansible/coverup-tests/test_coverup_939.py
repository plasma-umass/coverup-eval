# file: lib/ansible/parsing/dataloader.py:78-80
# asked: {"lines": [80], "branches": []}
# gained: {"lines": [80], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError

class MockVault:
    secrets = "mock_secrets"

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = MockVault()
    return loader

def test_load_yaml_data(dataloader):
    yaml_data = """
    key: value
    """
    result = dataloader.load(yaml_data)
    assert result == {'key': 'value'}

def test_load_json_data(dataloader):
    json_data = '{"key": "value"}'
    result = dataloader.load(json_data)
    assert result == {'key': 'value'}

def test_load_invalid_json_with_json_only(dataloader):
    invalid_json_data = '{"key": "value"'
    with pytest.raises(AnsibleParserError):
        dataloader.load(invalid_json_data, json_only=True)

def test_load_invalid_json_and_yaml(dataloader):
    invalid_data = '{"key": "value"'
    with pytest.raises(AnsibleParserError):
        dataloader.load(invalid_data, json_only=False)
