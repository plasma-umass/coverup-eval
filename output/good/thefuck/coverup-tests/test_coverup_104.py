# file thefuck/entrypoints/not_configured.py:75-79
# lines [75, 77, 78, 79]
# branches []

import pytest
from pathlib import Path
from unittest.mock import mock_open, patch
from thefuck.entrypoints.not_configured import _is_already_configured

@pytest.fixture
def mock_configuration_details(tmp_path):
    class ConfigurationDetails:
        def __init__(self, path, content):
            self.path = path
            self.content = content

    config_file = tmp_path / "shell_config"
    config_file.write_text("alias thefuck='eval $(thefuck $(fc -ln -1))'")
    return ConfigurationDetails(str(config_file), "alias thefuck='eval $(thefuck $(fc -ln -1))'")

def test_is_already_configured_true(mock_configuration_details):
    assert _is_already_configured(mock_configuration_details) == True

def test_is_already_configured_false(mock_configuration_details):
    # Change the content to ensure it does not match the file content
    mock_configuration_details.content = "some other content"
    with patch("builtins.open", mock_open(read_data="alias thefuck='eval $(thefuck $(fc -ln -1))'")):
        assert _is_already_configured(mock_configuration_details) == False
