# file: lib/ansible/config/manager.py:569-607
# asked: {"lines": [579, 588, 593, 603, 604], "branches": [[572, 575], [575, 578], [578, 579], [587, 588]]}
# gained: {"lines": [579, 588, 593, 603, 604], "branches": [[572, 575], [575, 578], [578, 579], [587, 588]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager, Setting
from ansible.errors import AnsibleOptionsError, AnsibleError

@pytest.fixture
def config_manager():
    cm = ConfigManager()
    cm._base_defs = {'some_key': {'type': 'string'}}
    cm._config_file = 'default_config_file'
    cm.data = MagicMock()
    cm.get_config_value_and_origin = MagicMock(return_value=('some_value', 'some_origin'))
    return cm

def test_update_config_data_defs_none(config_manager):
    config_manager.update_config_data(defs=None, configfile='some_config_file')
    config_manager.data.update_setting.assert_any_call(Setting('CONFIG_FILE', 'some_config_file', '', 'string'))

def test_update_config_data_configfile_none(config_manager):
    config_manager.update_config_data(defs={'some_key': {'type': 'string'}}, configfile=None)
    config_manager.data.update_setting.assert_any_call(Setting('CONFIG_FILE', 'default_config_file', '', 'string'))

def test_update_config_data_invalid_defs_type(config_manager):
    with pytest.raises(AnsibleOptionsError, match="Invalid configuration definition type: <class 'list'> for \[\]"):
        config_manager.update_config_data(defs=[], configfile='some_config_file')

def test_update_config_data_invalid_defs_content_type(config_manager):
    with pytest.raises(AnsibleOptionsError, match="Invalid configuration definition 'some_key': type is <class 'str'>"):
        config_manager.update_config_data(defs={'some_key': 'invalid_type'}, configfile='some_config_file')

def test_update_config_data_exception_handling(config_manager):
    config_manager.get_config_value_and_origin.side_effect = Exception('Test exception')
    with patch('sys.stderr.write') as mock_stderr:
        with pytest.raises(AnsibleError, match="Invalid settings supplied for some_key: Test exception"):
            config_manager.update_config_data(defs={'some_key': {'type': 'string'}}, configfile='some_config_file')
        mock_stderr.assert_called_once()
