# file semantic_release/settings.py:20-32
# lines [20, 21, 22, 23, 24, 26, 28, 29, 32]
# branches []

import os
import pytest
from unittest.mock import patch, mock_open
from semantic_release.settings import _config

@pytest.fixture
def mock_getcwd(mocker):
    mocker.patch('semantic_release.settings.getcwd', return_value='/mocked/path')

@pytest.fixture
def mock_config_from_ini(mocker):
    return mocker.patch('semantic_release.settings._config_from_ini', return_value={'key_ini': 'value_ini'})

@pytest.fixture
def mock_config_from_pyproject(mocker):
    return mocker.patch('semantic_release.settings._config_from_pyproject', return_value={'key_toml': 'value_toml'})

def test_config(mock_getcwd, mock_config_from_ini, mock_config_from_pyproject):
    config = _config()
    assert config['key_ini'] == 'value_ini'
    assert config['key_toml'] == 'value_toml'
