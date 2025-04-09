# file: lib/ansible/config/manager.py:316-341
# asked: {"lines": [316, 320, 321, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341], "branches": [[320, 321], [320, 323], [324, 0], [324, 325], [325, 326], [325, 341]]}
# gained: {"lines": [316, 320, 321, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341], "branches": [[320, 321], [320, 323], [324, 0], [324, 325], [325, 326], [325, 341]]}

import pytest
import configparser
from unittest.mock import mock_open, patch
from ansible.config.manager import ConfigManager, AnsibleOptionsError
from ansible.module_utils._text import to_bytes, to_text, to_native

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_parse_config_file_ini(config_manager, monkeypatch):
    cfile = 'test.ini'
    ini_content = "[section]\nkey=value\n"
    
    def mock_get_config_type(file):
        return 'ini'
    
    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)
    monkeypatch.setattr('builtins.open', mock_open(read_data=ini_content))
    
    config_manager._parsers = {}
    config_manager._parse_config_file(cfile)
    
    assert cfile in config_manager._parsers
    assert config_manager._parsers[cfile]['section']['key'] == 'value'

def test_parse_config_file_ini_unicode_error(config_manager, monkeypatch):
    cfile = 'test.ini'
    
    def mock_get_config_type(file):
        return 'ini'
    
    def mock_open_unicode_error(file, mode):
        m = mock_open()
        f = m(file, mode)
        f.read.side_effect = UnicodeError("mocked error")
        return f
    
    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)
    monkeypatch.setattr('builtins.open', mock_open_unicode_error)
    
    with pytest.raises(AnsibleOptionsError, match="Error reading config file"):
        config_manager._parse_config_file(cfile)

def test_parse_config_file_ini_configparser_error(config_manager, monkeypatch):
    cfile = 'test.ini'
    ini_content = "[section\nkey=value\n"  # malformed ini content
    
    def mock_get_config_type(file):
        return 'ini'
    
    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)
    monkeypatch.setattr('builtins.open', mock_open(read_data=ini_content))
    
    with pytest.raises(AnsibleOptionsError, match="Error reading config file"):
        config_manager._parse_config_file(cfile)

def test_parse_config_file_unsupported_type(config_manager, monkeypatch):
    cfile = 'test.unsupported'
    
    def mock_get_config_type(file):
        return 'unsupported'
    
    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)
    
    with pytest.raises(AnsibleOptionsError, match="Unsupported configuration file type"):
        config_manager._parse_config_file(cfile)
