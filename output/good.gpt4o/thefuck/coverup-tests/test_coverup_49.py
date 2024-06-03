# file thefuck/entrypoints/not_configured.py:75-79
# lines [75, 77, 78, 79]
# branches []

import pytest
from unittest.mock import mock_open, patch
from pathlib import Path

# Assuming the function _is_already_configured is imported from thefuck.entrypoints.not_configured
from thefuck.entrypoints.not_configured import _is_already_configured

class ConfigurationDetails:
    def __init__(self, path, content):
        self.path = path
        self.content = content

@pytest.fixture
def mock_path_open(mocker):
    return mocker.patch("pathlib.Path.open", mock_open(read_data="alias fuck='thefuck'"))

def test_is_already_configured(mock_path_open):
    config_details = ConfigurationDetails(path="~/.bashrc", content="alias fuck='thefuck'")
    assert _is_already_configured(config_details) == True

    config_details = ConfigurationDetails(path="~/.bashrc", content="alias notfuck='thenotfuck'")
    assert _is_already_configured(config_details) == False
