# file httpie/config.py:20-55
# lines [20, 35, 36, 37, 40, 41, 43, 46, 47, 48, 51, 52, 53, 55]
# branches ['36->37', '36->40', '40->41', '40->43', '47->48', '47->51']

import os
import pytest
from pathlib import Path
from unittest import mock
from httpie.config import get_default_config_dir, ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

@pytest.fixture
def mock_env(mocker):
    original_env = os.environ.copy()
    yield mocker.patch.dict(os.environ, {}, clear=True)
    os.environ.clear()
    os.environ.update(original_env)

@pytest.fixture
def mock_home(mocker):
    original_home = Path.home()
    mock_home = mocker.patch('pathlib.Path.home', return_value=Path('/mock/home'))
    yield mock_home
    mock_home.return_value = original_home

def test_get_default_config_dir_env_set(mock_env):
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/mock/config/dir'
    config_dir = get_default_config_dir()
    assert config_dir == Path('/mock/config/dir')

def test_get_default_config_dir_windows(mock_env, mocker):
    mocker.patch('httpie.config.is_windows', True)
    config_dir = get_default_config_dir()
    assert config_dir == DEFAULT_WINDOWS_CONFIG_DIR

def test_get_default_config_dir_legacy_exists(mock_env, mock_home, mocker):
    legacy_path = Path('/mock/home') / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    mocker.patch('pathlib.Path.exists', return_value=True)
    config_dir = get_default_config_dir()
    assert config_dir == legacy_path

def test_get_default_config_dir_xdg_explicit(mock_env, mock_home):
    os.environ[ENV_XDG_CONFIG_HOME] = '/mock/xdg/config'
    config_dir = get_default_config_dir()
    assert config_dir == Path('/mock/xdg/config') / DEFAULT_CONFIG_DIRNAME

def test_get_default_config_dir_xdg_default(mock_env, mock_home):
    config_dir = get_default_config_dir()
    expected_dir = Path('/mock/home') / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    assert config_dir == expected_dir
