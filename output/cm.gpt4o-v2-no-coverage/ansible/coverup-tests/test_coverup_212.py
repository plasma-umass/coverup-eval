# file: lib/ansible/plugins/action/reboot.py:235-257
# asked: {"lines": [235, 236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}
# gained: {"lines": [235, 236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    task = Mock()
    task.args = {}
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_boot_time_success(action_module):
    action_module._task.args = {'connect_timeout': 10}
    action_module._connection.set_option = Mock()
    action_module._connection.reset = Mock()
    action_module.get_system_boot_time = Mock(return_value="12345")
    
    action_module.check_boot_time('Linux', '1234')
    
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()
    action_module.get_system_boot_time.assert_called_with('Linux')

def test_check_boot_time_no_change(action_module):
    action_module.get_system_boot_time = Mock(return_value="1234")
    
    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('Linux', '1234')

def test_check_boot_time_empty_string(action_module):
    action_module.get_system_boot_time = Mock(return_value="")
    
    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('Linux', '1234')

def test_check_boot_time_exception(action_module):
    action_module.get_system_boot_time = Mock(side_effect=Exception("error"))
    
    with pytest.raises(Exception, match="error"):
        action_module.check_boot_time('Linux', '1234')

def test_check_boot_time_attribute_error(action_module):
    action_module._task.args = {'connect_timeout': 10}
    action_module._connection.set_option = Mock(side_effect=AttributeError)
    action_module._connection.reset = Mock()
    action_module.get_system_boot_time = Mock(return_value="12345")
    
    with patch('ansible.plugins.action.reboot.display.warning') as mock_warning:
        action_module.check_boot_time('Linux', '1234')
        mock_warning.assert_called_once_with("Connection plugin does not allow the connection timeout to be overridden")
        action_module.get_system_boot_time.assert_called_with('Linux')
