# file: pytutils/log.py:100-128
# asked: {"lines": [101, 103, 104, 106, 107, 109, 110, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125, 128], "branches": [[103, 104], [103, 106], [106, 107], [106, 109], [109, 110], [109, 112], [112, 113], [112, 128]]}
# gained: {"lines": [101, 103, 104, 106, 107, 109, 110, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125, 128], "branches": [[103, 104], [103, 106], [106, 107], [106, 109], [109, 110], [109, 112], [112, 113], [112, 128]]}

import os
import pytest
from unittest import mock

# Assuming the function get_config is imported from pytutils.log
from pytutils.log import get_config

def test_get_config_given():
    config = {'key': 'value'}
    result = get_config(given=config)
    assert result == config

def test_get_config_env_var(monkeypatch):
    monkeypatch.setenv('TEST_ENV_VAR', '{"key": "value"}')
    result = get_config(env_var='TEST_ENV_VAR')
    assert result == {"key": "value"}

def test_get_config_default():
    default_config = {'key': 'value'}
    result = get_config(default=default_config)
    assert result == default_config

def test_get_config_none():
    with pytest.raises(ValueError, match='Invalid logging config: None'):
        get_config()

def test_get_config_json_string():
    json_config = '{"key": "value"}'
    result = get_config(given=json_config)
    assert result == {"key": "value"}

def test_get_config_invalid_json(mocker):
    invalid_json = '{"key": "value"'
    mocker.patch('json.loads', side_effect=ValueError)
    mocker.patch('yaml.load', return_value={"key": "value"})
    result = get_config(given=invalid_json)
    assert result == {"key": "value"}

def test_get_config_invalid_yaml(mocker):
    invalid_yaml = 'key: value:'
    mocker.patch('json.loads', side_effect=ValueError)
    mocker.patch('yaml.load', side_effect=ValueError)
    with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: key: value:"):
        get_config(given=invalid_yaml)
