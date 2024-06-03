# file httpie/config.py:131-144
# lines [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.config import Config, DEFAULT_CONFIG_DIR

@pytest.fixture
def mock_base_config_dict(mocker):
    mocker.patch('httpie.config.BaseConfigDict.__init__', return_value=None)
    mocker.patch('httpie.config.BaseConfigDict.update', MagicMock())
    mocker.patch('httpie.config.BaseConfigDict.__getitem__', MagicMock())

def test_config_initialization(mock_base_config_dict):
    config = Config()
    assert config.directory == Path(DEFAULT_CONFIG_DIR)
    config.update.assert_called_once_with({'default_options': []})

def test_config_custom_directory(mock_base_config_dict):
    custom_dir = '/custom/config/dir'
    config = Config(directory=custom_dir)
    assert config.directory == Path(custom_dir)
    config.update.assert_called_once_with({'default_options': []})

def test_default_options_property(mock_base_config_dict):
    config = Config()
    config.__getitem__.return_value = ['--verbose']
    assert config.default_options == ['--verbose']
