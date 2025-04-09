# file: lib/ansible/plugins/action/reboot.py:405-465
# asked: {"lines": [405, 406, 407, 410, 411, 412, 414, 415, 417, 418, 420, 422, 424, 425, 427, 430, 431, 432, 433, 434, 435, 436, 439, 440, 441, 442, 443, 444, 446, 448, 449, 450, 451, 452, 454, 455, 456, 457, 460, 462, 463, 465], "branches": [[410, 411], [410, 414], [414, 415], [414, 417], [417, 418], [417, 420], [424, 425], [424, 427], [448, 449], [448, 454], [454, 455], [454, 460]]}
# gained: {"lines": [405, 406, 407, 410, 411, 412, 414, 415, 417, 418, 420, 422, 424, 427, 430, 431, 432, 433, 434, 435, 436, 439, 440, 441, 442, 446, 448, 449, 450, 451, 452, 454, 455, 456, 457, 460, 462, 463, 465], "branches": [[410, 411], [410, 414], [414, 415], [414, 417], [417, 418], [417, 420], [424, 427], [448, 449], [448, 454], [454, 455]]}

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock()
    )

def test_run_local_connection(action_module):
    action_module._connection.transport = 'local'
    action_module._task.action = 'reboot'
    result = action_module.run()
    assert result == {
        'changed': False,
        'elapsed': 0,
        'rebooted': False,
        'failed': True,
        'msg': 'Running reboot with local connection would reboot the control node.'
    }

def test_run_check_mode(action_module):
    action_module._connection.transport = 'ssh'
    action_module._play_context.check_mode = True
    result = action_module.run()
    assert result == {
        'changed': True,
        'elapsed': 0,
        'rebooted': True
    }

def test_run_task_vars_none(action_module):
    action_module._connection.transport = 'ssh'
    action_module._play_context.check_mode = False
    action_module.deprecated_args = MagicMock()
    action_module.get_distribution = MagicMock(return_value='distribution')
    action_module.get_system_boot_time = MagicMock(return_value='boot_time')
    action_module.perform_reboot = MagicMock(return_value={'failed': False, 'start': datetime.utcnow()})
    action_module.validate_reboot = MagicMock(return_value={'rebooted': True, 'changed': True})
    result = action_module.run()
    assert 'changed' in result
    assert 'elapsed' in result
    assert 'rebooted' in result

def test_run_task_vars_not_none(action_module):
    action_module._connection.transport = 'ssh'
    action_module._play_context.check_mode = False
    action_module.deprecated_args = MagicMock()
    action_module.get_distribution = MagicMock(return_value='distribution')
    action_module.get_system_boot_time = MagicMock(return_value='boot_time')
    action_module.perform_reboot = MagicMock(return_value={'failed': False, 'start': datetime.utcnow()})
    action_module.validate_reboot = MagicMock(return_value={'rebooted': True, 'changed': True})
    result = action_module.run(task_vars={'some_var': 'some_value'})
    assert 'changed' in result
    assert 'elapsed' in result
    assert 'rebooted' in result

def test_run_reboot_failed(action_module):
    action_module._connection.transport = 'ssh'
    action_module._play_context.check_mode = False
    action_module.deprecated_args = MagicMock()
    action_module.get_distribution = MagicMock(return_value='distribution')
    action_module.get_system_boot_time = MagicMock(return_value='boot_time')
    action_module.perform_reboot = MagicMock(return_value={'failed': True, 'start': datetime.utcnow()})
    result = action_module.run()
    assert result['failed'] == True
    assert 'elapsed' in result

def test_run_exception_in_get_system_boot_time(action_module):
    action_module._connection.transport = 'ssh'
    action_module._play_context.check_mode = False
    action_module.deprecated_args = MagicMock()
    action_module.get_distribution = MagicMock(return_value='distribution')
    action_module.get_system_boot_time = MagicMock(side_effect=Exception('error'))
    result = action_module.run()
    assert result['failed'] == True
    assert result['reboot'] == False
    assert 'msg' in result
