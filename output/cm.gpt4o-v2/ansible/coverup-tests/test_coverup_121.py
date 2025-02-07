# file: lib/ansible/config/manager.py:316-341
# asked: {"lines": [316, 320, 321, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341], "branches": [[320, 321], [320, 323], [324, 0], [324, 325], [325, 326], [325, 341]]}
# gained: {"lines": [316, 320, 321, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341], "branches": [[320, 321], [324, 0], [324, 325], [325, 326], [325, 341]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_text, to_bytes, to_native
from ansible.module_utils.six.moves import configparser
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    cm = ConfigManager()
    cm._config_file = 'default.ini'
    cm._parsers = {}
    return cm

def test_parse_config_file_ini(config_manager):
    mock_data = "[section]\nkey=value"
    with patch("builtins.open", mock_open(read_data=mock_data)), \
         patch("ansible.config.manager.to_bytes", return_value=b"default.ini"), \
         patch("ansible.config.manager.get_config_type", return_value="ini"):
        config_manager._parse_config_file()
        assert 'default.ini' in config_manager._parsers
        assert config_manager._parsers['default.ini'].get('section', 'key') == 'value'

def test_parse_config_file_unsupported_type(config_manager):
    with patch("ansible.config.manager.get_config_type", return_value="unsupported"):
        with pytest.raises(AnsibleOptionsError, match="Unsupported configuration file type"):
            config_manager._parse_config_file()

def test_parse_config_file_unicode_error(config_manager):
    with patch("builtins.open", mock_open(read_data=b"\x80abc")), \
         patch("ansible.config.manager.to_bytes", return_value=b"default.ini"), \
         patch("ansible.config.manager.get_config_type", return_value="ini"), \
         patch("ansible.config.manager.to_text", side_effect=UnicodeError("utf-8 codec can't decode byte 0x80")):
        with pytest.raises(AnsibleOptionsError, match="config file was not utf8 encoded"):
            config_manager._parse_config_file()

def test_parse_config_file_configparser_error(config_manager):
    mock_data = "[section\nkey=value"  # malformed ini
    with patch("builtins.open", mock_open(read_data=mock_data)), \
         patch("ansible.config.manager.to_bytes", return_value=b"default.ini"), \
         patch("ansible.config.manager.get_config_type", return_value="ini"):
        with pytest.raises(AnsibleOptionsError, match="Error reading config file"):
            config_manager._parse_config_file()
