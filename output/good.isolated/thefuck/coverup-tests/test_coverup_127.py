# file thefuck/conf.py:44-56
# lines [46, 47, 48, 51, 52, 53, 54, 56]
# branches ['51->52', '51->56']

import os
from pathlib import Path
from unittest.mock import patch
import pytest
from thefuck.conf import Settings

@pytest.fixture
def clean_env(mocker):
    # Use mocker to ensure environment is clean after the test
    mocker.patch.dict(os.environ, {}, clear=True)

def test_get_user_dir_path_legacy(clean_env):
    # Setup: create a temporary legacy directory
    legacy_user_dir = Path.home() / '.thefuck'
    legacy_user_dir.mkdir(parents=True, exist_ok=True)

    # Ensure the directory is removed after the test
    try:
        settings = Settings()
        with patch('thefuck.conf.warn') as mock_warn:
            result = settings._get_user_dir_path()

            # Assertions to check if the legacy path is returned
            assert result == legacy_user_dir
            mock_warn.assert_called_once()
    finally:
        # Cleanup: remove the temporary legacy directory
        legacy_user_dir.rmdir()

def test_get_user_dir_path_xdg(clean_env):
    # Setup: define a fake XDG_CONFIG_HOME
    fake_xdg_config_home = '/fake/xdg/config'
    os.environ['XDG_CONFIG_HOME'] = fake_xdg_config_home
    user_dir = Path(fake_xdg_config_home) / 'thefuck'
    user_dir.mkdir(parents=True, exist_ok=True)

    # Ensure the directory is removed after the test
    try:
        settings = Settings()
        result = settings._get_user_dir_path()

        # Assertions to check if the XDG path is returned
        assert result == user_dir
    finally:
        # Cleanup: remove the fake XDG_CONFIG_HOME directory
        user_dir.rmdir()
