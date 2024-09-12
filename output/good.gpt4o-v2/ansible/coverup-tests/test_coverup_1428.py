# file: lib/ansible/config/manager.py:316-341
# asked: {"lines": [], "branches": [[320, 323]]}
# gained: {"lines": [], "branches": [[320, 323]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_text, to_bytes, to_native
from ansible.module_utils.six.moves import configparser
from ansible.config.manager import ConfigManager

def test_parse_config_file_with_default_cfile(monkeypatch):
    config_manager = ConfigManager()
    config_manager._config_file = 'test.ini'
    config_manager._parsers = {}

    def mock_get_config_type(cfile):
        return 'ini'

    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)
    mock_file_data = "[default]\noption=value"

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        config_manager._parse_config_file()

    assert 'test.ini' in config_manager._parsers
    assert config_manager._parsers['test.ini'].get('default', 'option') == 'value'

def test_parse_config_file_with_unsupported_type(monkeypatch):
    config_manager = ConfigManager()
    config_manager._parsers = {}

    def mock_get_config_type(cfile):
        return 'unsupported'

    monkeypatch.setattr('ansible.config.manager.get_config_type', mock_get_config_type)

    with pytest.raises(AnsibleOptionsError, match="Unsupported configuration file type"):
        config_manager._parse_config_file('test.unsupported')
