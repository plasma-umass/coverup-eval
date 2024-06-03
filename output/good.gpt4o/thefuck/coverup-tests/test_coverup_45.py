# file thefuck/shells/generic.py:149-154
# lines [149, 150, 151, 152, 153, 154]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from thefuck.shells.generic import Generic

class ShellConfiguration:
    def __init__(self, content, path, reload, can_configure_automatically):
        self.content = content
        self.path = path
        self.reload = reload
        self.can_configure_automatically = can_configure_automatically

def test_create_shell_configuration(mocker):
    generic = Generic()
    content = "test content"
    path = "~/test_path"
    reload = True

    # Mock Path.expanduser().exists() to return True
    mock_expanduser = mocker.patch('pathlib.Path.expanduser', return_value=Path('/mocked_path'))
    mock_exists = mocker.patch('pathlib.Path.exists', return_value=True)

    config = generic._create_shell_configuration(content, path, reload)

    assert config.content == content
    assert config.path == path
    assert config.reload == reload
    assert config.can_configure_automatically == True

    # Clean up mocks
    mock_expanduser.stop()
    mock_exists.stop()

    # Mock Path.expanduser().exists() to return False
    mock_expanduser = mocker.patch('pathlib.Path.expanduser', return_value=Path('/mocked_path'))
    mock_exists = mocker.patch('pathlib.Path.exists', return_value=False)

    config = generic._create_shell_configuration(content, path, reload)

    assert config.content == content
    assert config.path == path
    assert config.reload == reload
    assert config.can_configure_automatically == False

    # Clean up mocks
    mock_expanduser.stop()
    mock_exists.stop()
