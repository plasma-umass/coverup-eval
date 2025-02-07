# file: pytutils/log.py:100-128
# asked: {"lines": [107, 110, 117, 118, 120, 121, 122, 123, 124, 125], "branches": [[103, 106], [106, 107], [109, 110], [112, 128]]}
# gained: {"lines": [107, 110, 117, 118, 120, 121, 122, 123, 124, 125], "branches": [[103, 106], [106, 107], [109, 110], [112, 128]]}

import os
import pytest
import json
import yaml
from pytutils.log import get_config

def test_get_config_with_given():
    config = {"key": "value"}
    assert get_config(given=config) == config

def test_get_config_with_env_var(monkeypatch):
    monkeypatch.setenv("TEST_ENV_VAR", '{"key": "value"}')
    assert get_config(env_var="TEST_ENV_VAR") == {"key": "value"}

def test_get_config_with_default():
    default_config = {"key": "value"}
    assert get_config(default=default_config) == default_config

def test_get_config_with_none():
    with pytest.raises(ValueError, match="Invalid logging config: None"):
        get_config()

def test_get_config_with_json_string():
    json_config = '{"key": "value"}'
    assert get_config(given=json_config) == {"key": "value"}

def test_get_config_with_invalid_json_but_valid_yaml_string(monkeypatch):
    yaml_config = "key: value"
    monkeypatch.setattr(yaml, 'load', lambda x, Loader=None: {"key": "value"})
    assert get_config(given=yaml_config) == {"key": "value"}

def test_get_config_with_invalid_json_and_yaml_string(monkeypatch):
    invalid_config = "invalid config"
    def mock_yaml_load(x, Loader=None):
        raise ValueError("Invalid YAML")
    monkeypatch.setattr(yaml, 'load', mock_yaml_load)
    with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid config"):
        get_config(given=invalid_config)
