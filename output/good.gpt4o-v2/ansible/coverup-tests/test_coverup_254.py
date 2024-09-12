# file: lib/ansible/parsing/utils/yaml.py:59-84
# asked: {"lines": [59, 64, 66, 68, 72, 73, 75, 76, 79, 80, 81, 82, 84], "branches": [[75, 76], [75, 79]]}
# gained: {"lines": [59, 64, 66, 68, 72, 73, 75, 76, 79, 80, 81, 82, 84], "branches": [[75, 76], [75, 79]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.utils.yaml import from_yaml
from ansible.errors import AnsibleParserError
from yaml import YAMLError

def test_from_yaml_json_only():
    data = '{"key": "value"}'
    result = from_yaml(data, json_only=True)
    assert result == {"key": "value"}

def test_from_yaml_invalid_json_json_only():
    data = 'invalid json'
    with pytest.raises(AnsibleParserError):
        from_yaml(data, json_only=True)

def test_from_yaml_yaml():
    data = 'key: value'
    result = from_yaml(data)
    assert result == {"key": "value"}

def test_from_yaml_invalid_json_valid_yaml():
    data = 'key: value'
    with patch('ansible.parsing.utils.yaml._safe_load', return_value={"key": "value"}) as mock_safe_load:
        result = from_yaml(data)
        mock_safe_load.assert_called_once_with(data, file_name='<string>', vault_secrets=None)
        assert result == {"key": "value"}

def test_from_yaml_invalid_json_invalid_yaml():
    data = 'invalid json and yaml'
    with patch('ansible.parsing.utils.yaml._safe_load', side_effect=YAMLError), \
         patch('ansible.parsing.utils.yaml._handle_error') as mock_handle_error:
        from_yaml(data)
        mock_handle_error.assert_called_once()

def test_from_yaml_with_vault_secrets():
    data = '{"key": "value"}'
    vault_secrets = "vault_secret"
    with patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets') as mock_set_secrets:
        result = from_yaml(data, vault_secrets=vault_secrets)
        mock_set_secrets.assert_called_once_with(vault_secrets)
        assert result == {"key": "value"}
