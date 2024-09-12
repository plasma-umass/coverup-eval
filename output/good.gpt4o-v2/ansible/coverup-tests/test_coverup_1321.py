# file: lib/ansible/parsing/dataloader.py:78-80
# asked: {"lines": [80], "branches": []}
# gained: {"lines": [80], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError
from ansible.parsing.ajson import AnsibleJSONDecoder

@pytest.fixture
def mock_vault():
    class MockVault:
        secrets = "mock_secrets"
    return MockVault()

def test_load_yaml_data(mock_vault):
    data_loader = DataLoader()
    data_loader._vault = mock_vault

    yaml_data = """
    key: value
    """
    with patch('ansible.parsing.utils.yaml._safe_load', return_value={"key": "value"}) as mock_safe_load:
        result = data_loader.load(yaml_data, json_only=False)
        mock_safe_load.assert_called_once_with(yaml_data, file_name='<string>', vault_secrets="mock_secrets")
        assert result == {"key": "value"}

def test_load_json_data(mock_vault):
    data_loader = DataLoader()
    data_loader._vault = mock_vault

    json_data = '{"key": "value"}'
    with patch('ansible.parsing.utils.yaml.json.loads', return_value={"key": "value"}) as mock_json_loads:
        result = data_loader.load(json_data, json_only=True)
        mock_json_loads.assert_called_once_with(json_data, cls=AnsibleJSONDecoder)
        assert result == {"key": "value"}

def test_load_json_data_with_exception(mock_vault):
    data_loader = DataLoader()
    data_loader._vault = mock_vault

    invalid_json_data = 'invalid json'
    with patch('ansible.parsing.utils.yaml.json.loads', side_effect=Exception("json error")), \
         patch('ansible.parsing.utils.yaml._safe_load', return_value={"key": "value"}) as mock_safe_load:
        result = data_loader.load(invalid_json_data, json_only=False)
        mock_safe_load.assert_called_once_with(invalid_json_data, file_name='<string>', vault_secrets="mock_secrets")
        assert result == {"key": "value"}

def test_load_json_data_with_json_only_exception(mock_vault):
    data_loader = DataLoader()
    data_loader._vault = mock_vault

    invalid_json_data = 'invalid json'
    with patch('ansible.parsing.utils.yaml.json.loads', side_effect=Exception("json error")):
        with pytest.raises(AnsibleParserError):
            data_loader.load(invalid_json_data, json_only=True)
