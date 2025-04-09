# file httpie/config.py:20-55
# lines [37, 41, 48]
# branches ['36->37', '40->41', '47->48']

import os
import pytest
from pathlib import Path
from httpie.config import get_default_config_dir, ENV_HTTPIE_CONFIG_DIR, DEFAULT_WINDOWS_CONFIG_DIR

@pytest.fixture
def mock_env(mocker):
    return mocker.patch.dict(os.environ, {})

@pytest.fixture
def mock_home(mocker):
    return mocker.patch('pathlib.Path.home')

@pytest.fixture
def mock_is_windows(mocker):
    return mocker.patch('httpie.config.is_windows')

def test_get_default_config_dir_env_set(mock_env):
    test_dir = '/test/httpie/config'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = test_dir
    assert get_default_config_dir() == Path(test_dir)

def test_get_default_config_dir_windows(mock_is_windows, mock_env, mock_home):
    mock_is_windows.return_value = True
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

def test_get_default_config_dir_legacy(mock_env, mock_home, tmp_path):
    mock_home.return_value = tmp_path
    legacy_dir = tmp_path / '.httpie'
    legacy_dir.mkdir()
    assert get_default_config_dir() == legacy_dir
