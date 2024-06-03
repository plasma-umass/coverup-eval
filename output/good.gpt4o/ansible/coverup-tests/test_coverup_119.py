# file lib/ansible/config/manager.py:569-607
# lines [569, 572, 573, 575, 576, 578, 579, 582, 584, 586, 587, 588, 591, 592, 593, 603, 604, 607]
# branches ['572->573', '572->575', '575->576', '575->578', '578->579', '578->582', '586->exit', '586->587', '587->588', '587->591']

import pytest
from unittest.mock import Mock, patch
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError, AnsibleError
import sys
import traceback

class Setting:
    def __init__(self, name, value, origin, type):
        self.name = name
        self.value = value
        self.origin = origin
        self.type = type

    def __eq__(self, other):
        return (self.name, self.value, self.origin, self.type) == (other.name, other.value, other.origin, other.type)

@pytest.fixture
def config_manager():
    cm = ConfigManager()
    cm._base_defs = {'DEFAULT': {'type': 'string'}}
    cm._config_file = 'default_config_file'
    cm.data = Mock()
    cm.get_config_value_and_origin = Mock(return_value=('value', 'origin'))
    return cm

def test_update_config_data_no_defs_no_configfile(config_manager):
    config_manager.update_config_data()
    config_manager.data.update_setting.assert_any_call(Setting('CONFIG_FILE', 'default_config_file', '', 'string'))

def test_update_config_data_invalid_defs_type(config_manager):
    with pytest.raises(AnsibleOptionsError, match="Invalid configuration definition type: <class 'str'> for invalid_defs"):
        config_manager.update_config_data(defs='invalid_defs')

def test_update_config_data_invalid_config_def(config_manager):
    with pytest.raises(AnsibleOptionsError, match="Invalid configuration definition 'DEFAULT': type is <class 'str'>"):
        config_manager.update_config_data(defs={'DEFAULT': 'invalid_def'})

def test_update_config_data_exception_handling(config_manager, mocker):
    mocker.patch('sys.stderr.write')
    config_manager.get_config_value_and_origin.side_effect = Exception('Test Exception')
    with pytest.raises(AnsibleError, match="Invalid settings supplied for DEFAULT: Test Exception"):
        config_manager.update_config_data(defs={'DEFAULT': {'type': 'string'}})
    sys.stderr.write.assert_called_once()
    assert "Unhandled error:\n" in sys.stderr.write.call_args[0][0]
    assert "Exception: Test Exception" in sys.stderr.write.call_args[0][0]
