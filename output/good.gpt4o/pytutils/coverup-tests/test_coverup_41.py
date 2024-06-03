# file pytutils/log.py:100-128
# lines [104, 107, 110, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125]
# branches ['103->104', '106->107', '109->110', '112->113']

import os
import pytest
from unittest import mock
from pytutils.log import get_config

def test_get_config_env_var(mocker):
    mocker.patch.dict(os.environ, {'TEST_ENV_VAR': '{"key": "value"}'})
    config = get_config(env_var='TEST_ENV_VAR')
    assert config == {"key": "value"}

def test_get_config_default():
    config = get_config(default='{"key": "value"}')
    assert config == {"key": "value"}

def test_get_config_invalid():
    with pytest.raises(ValueError, match='Invalid logging config: None'):
        get_config()

def test_get_config_invalid_json(mocker):
    mocker.patch('yaml.load', side_effect=ValueError)
    with pytest.raises(ValueError, match='Could not parse logging config as bare, json, or yaml: invalid_json'):
        get_config(given='invalid_json')

def test_get_config_yaml(mocker):
    mocker.patch('yaml.load', return_value={"key": "value"})
    config = get_config(given='key: value')
    assert config == {"key": "value"}
