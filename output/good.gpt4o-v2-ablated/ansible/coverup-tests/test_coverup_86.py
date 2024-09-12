# file: lib/ansible/config/manager.py:282-304
# asked: {"lines": [282, 284, 285, 286, 288, 289, 291, 292, 294, 296, 299, 301, 304], "branches": [[294, 296], [294, 299], [299, 301], [299, 304]]}
# gained: {"lines": [282, 284, 285, 286, 288, 289, 291, 292, 294, 296, 299, 301, 304], "branches": [[294, 296], [294, 299], [299, 301]]}

import os
import pytest
from unittest import mock
from ansible.config.manager import ConfigManager

@pytest.fixture
def mock_config_data():
    with mock.patch('ansible.config.manager.ConfigData') as MockConfigData:
        yield MockConfigData

@pytest.fixture
def mock_read_config_yaml_file():
    with mock.patch('ansible.config.manager.ConfigManager._read_config_yaml_file') as mock_read:
        mock_read.return_value = {}
        yield mock_read

@pytest.fixture
def mock_add_base_defs_deprecations():
    with mock.patch('ansible.config.manager._add_base_defs_deprecations') as mock_add:
        yield mock_add

@pytest.fixture
def mock_find_ini_config_file():
    with mock.patch('ansible.config.manager.find_ini_config_file') as mock_find:
        mock_find.return_value = 'dummy.ini'
        yield mock_find

@pytest.fixture
def mock_parse_config_file():
    with mock.patch('ansible.config.manager.ConfigManager._parse_config_file') as mock_parse:
        yield mock_parse

@pytest.fixture
def mock_update_config_data():
    with mock.patch('ansible.config.manager.ConfigManager.update_config_data') as mock_update:
        yield mock_update

def test_config_manager_with_conf_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_parse_config_file, mock_update_config_data):
    conf_file = 'test_conf.yml'
    defs_file = 'test_defs.yml'
    manager = ConfigManager(conf_file=conf_file, defs_file=defs_file)
    
    assert manager._config_file == conf_file
    assert mock_read_config_yaml_file.called_once_with(defs_file)
    assert mock_add_base_defs_deprecations.called_once()
    assert mock_parse_config_file.called_once()
    assert mock_update_config_data.called_once()

def test_config_manager_without_conf_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_parse_config_file, mock_update_config_data):
    defs_file = 'test_defs.yml'
    manager = ConfigManager(defs_file=defs_file)
    
    assert manager._config_file == 'dummy.ini'
    assert mock_read_config_yaml_file.called_once_with(defs_file)
    assert mock_add_base_defs_deprecations.called_once()
    assert mock_find_ini_config_file.called_once()
    assert mock_parse_config_file.called_once()
    assert mock_update_config_data.called_once()

def test_config_manager_no_files(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_parse_config_file, mock_update_config_data):
    manager = ConfigManager()
    
    expected_defs_file = '%s/base.yml' % os.path.dirname(__file__)
    assert manager._config_file == 'dummy.ini'
    assert mock_read_config_yaml_file.called_once_with(expected_defs_file)
    assert mock_add_base_defs_deprecations.called_once()
    assert mock_find_ini_config_file.called_once()
    assert mock_parse_config_file.called_once()
    assert mock_update_config_data.called_once()
