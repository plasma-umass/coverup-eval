# file semantic_release/settings.py:20-32
# lines [20, 21, 22, 23, 24, 26, 28, 29, 32]
# branches []

import os
from unittest.mock import patch
from semantic_release.settings import _config
import pytest

@pytest.fixture
def mock_cwd(tmp_path):
    with patch('semantic_release.settings.getcwd', return_value=str(tmp_path)):
        yield tmp_path

@pytest.fixture
def mock_ini_config():
    with patch('semantic_release.settings._config_from_ini', return_value={'ini_key': 'ini_value'}) as mock:
        yield mock

@pytest.fixture
def mock_toml_config():
    with patch('semantic_release.settings._config_from_pyproject', return_value={'toml_key': 'toml_value'}) as mock:
        yield mock

def test_config_combines_ini_and_toml(mock_cwd, mock_ini_config, mock_toml_config):
    config = _config()
    assert config.get('ini_key') == 'ini_value'
    assert config.get('toml_key') == 'toml_value'
    mock_ini_config.assert_called_once()
    mock_toml_config.assert_called_once()
