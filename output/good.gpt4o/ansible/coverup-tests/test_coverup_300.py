# file lib/ansible/parsing/utils/yaml.py:59-84
# lines [59, 64, 66, 68, 72, 73, 75, 76, 79, 80, 81, 82, 84]
# branches ['75->76', '75->79']

import pytest
from unittest import mock
from ansible.parsing.utils.yaml import from_yaml, AnsibleParserError, AnsibleJSONDecoder, _safe_load, _handle_error
import json
import yaml

def test_from_yaml_json_only(mocker):
    data = '{"key": "value"}'
    mocker.patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets')
    result = from_yaml(data, json_only=True)
    assert result == {"key": "value"}

def test_from_yaml_invalid_json_json_only(mocker):
    data = 'invalid json'
    mocker.patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets')
    with pytest.raises(AnsibleParserError):
        from_yaml(data, json_only=True)

def test_from_yaml_invalid_json_valid_yaml(mocker):
    data = 'key: value'
    mocker.patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets')
    mocker.patch('ansible.parsing.utils.yaml._safe_load', return_value={"key": "value"})
    result = from_yaml(data)
    assert result == {"key": "value"}

def test_from_yaml_invalid_json_invalid_yaml(mocker):
    data = 'invalid yaml: ['
    mocker.patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets')
    mock_safe_load = mocker.patch('ansible.parsing.utils.yaml._safe_load', side_effect=yaml.YAMLError)
    mock_handle_error = mocker.patch('ansible.parsing.utils.yaml._handle_error', side_effect=Exception)
    with pytest.raises(Exception):
        from_yaml(data)
    assert mock_safe_load.called
    assert mock_handle_error.called

def test_from_yaml_valid_json(mocker):
    data = '{"key": "value"}'
    mocker.patch('ansible.parsing.utils.yaml.AnsibleJSONDecoder.set_secrets')
    result = from_yaml(data)
    assert result == {"key": "value"}
