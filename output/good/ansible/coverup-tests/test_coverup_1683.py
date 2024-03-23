# file lib/ansible/config/manager.py:282-304
# lines [301]
# branches ['294->299', '299->301']

import os
import pytest
from ansible.config.manager import ConfigManager
from unittest.mock import MagicMock

# Assuming the existence of a function `find_ini_config_file` and a class `ConfigData`
# which are not provided in the snippet. They should be mocked for the test.

@pytest.fixture
def mock_find_ini_config_file(mocker):
    return mocker.patch('ansible.config.manager.find_ini_config_file', return_value='path/to/config.ini')

@pytest.fixture
def mock_parse_config_file(mocker):
    return mocker.patch.object(ConfigManager, '_parse_config_file')

@pytest.fixture
def mock_add_base_defs_deprecations(mocker):
    return mocker.patch('ansible.config.manager._add_base_defs_deprecations')

@pytest.fixture
def mock_read_config_yaml_file(mocker):
    return mocker.patch('ansible.config.manager.ConfigManager._read_config_yaml_file', return_value={})

@pytest.fixture
def cleanup():
    # Cleanup code if necessary
    yield
    # Perform cleanup after the test
    # e.g., remove created files, reset environment variables, etc.

def test_config_manager_reads_ini_when_no_conf_file(
    mock_find_ini_config_file, mock_parse_config_file, mock_add_base_defs_deprecations,
    mock_read_config_yaml_file, cleanup
):
    # Test to cover line 301 and branch 294->299
    cm = ConfigManager(conf_file=None)
    mock_find_ini_config_file.assert_called_once()
    mock_parse_config_file.assert_called_once()
    assert cm._config_file == 'path/to/config.ini'
