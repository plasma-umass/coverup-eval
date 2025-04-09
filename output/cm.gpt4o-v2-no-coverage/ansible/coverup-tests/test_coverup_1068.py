# file: lib/ansible/parsing/dataloader.py:78-80
# asked: {"lines": [78, 80], "branches": []}
# gained: {"lines": [78, 80], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError

def test_load_yaml_data(mocker):
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', return_value={'key': 'value'})
    data_loader = DataLoader()
    data = "key: value"
    result = data_loader.load(data)
    assert result == {'key': 'value'}

def test_load_json_data(mocker):
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', return_value={'key': 'value'})
    data_loader = DataLoader()
    data = '{"key": "value"}'
    result = data_loader.load(data)
    assert result == {'key': 'value'}

def test_load_invalid_json_with_json_only(mocker):
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', side_effect=AnsibleParserError("Invalid JSON"))
    data_loader = DataLoader()
    data = "invalid json"
    with pytest.raises(AnsibleParserError):
        data_loader.load(data, json_only=True)

def test_load_invalid_yaml(mocker):
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', side_effect=AnsibleParserError("Invalid YAML"))
    data_loader = DataLoader()
    data = "invalid: yaml: data"
    with pytest.raises(AnsibleParserError):
        data_loader.load(data)

def test_load_valid_yaml_invalid_json(mocker):
    def from_yaml_side_effect(data, file_name, show_content, vault_secrets, json_only):
        if data == "invalid json":
            raise AnsibleParserError("Invalid JSON")
        return {'key': 'value'}
    
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', side_effect=from_yaml_side_effect)
    data_loader = DataLoader()
    data = "key: value"
    result = data_loader.load(data, json_only=False)
    assert result == {'key': 'value'}

def test_load_valid_json_invalid_yaml(mocker):
    def from_yaml_side_effect(data, file_name, show_content, vault_secrets, json_only):
        if data == '{"key": "value"}':
            return {'key': 'value'}
        raise AnsibleParserError("Invalid YAML")
    
    mocker.patch('ansible.parsing.utils.yaml.from_yaml', side_effect=from_yaml_side_effect)
    data_loader = DataLoader()
    data = '{"key": "value"}'
    result = data_loader.load(data, json_only=False)
    assert result == {'key': 'value'}
