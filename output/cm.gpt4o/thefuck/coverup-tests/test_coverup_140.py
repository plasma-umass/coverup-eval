# file thefuck/conf.py:36-42
# lines [37, 38, 39, 40, 41, 42]
# branches ['38->exit', '38->39', '41->exit', '41->42']

import pytest
from unittest import mock
from pathlib import Path
from thefuck.conf import Settings
import thefuck.const as const

@pytest.fixture
def mock_user_dir(tmp_path):
    user_dir = tmp_path / "user"
    user_dir.mkdir()
    return user_dir

def test_init_settings_file(mock_user_dir, mocker):
    settings = Settings()
    settings.user_dir = mock_user_dir

    settings_path = mock_user_dir / 'settings.py'
    mocker.patch('thefuck.conf.const.SETTINGS_HEADER', '# Settings Header\n')
    mocker.patch('thefuck.conf.const.DEFAULT_SETTINGS', {'example_setting': 'example_value'})

    settings._init_settings_file()

    assert settings_path.is_file()
    with settings_path.open() as settings_file:
        content = settings_file.read()
        assert '# Settings Header\n' in content
        assert '# example_setting = example_value\n' in content
