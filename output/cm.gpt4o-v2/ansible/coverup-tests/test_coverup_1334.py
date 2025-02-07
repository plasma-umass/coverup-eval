# file: lib/ansible/plugins/action/reboot.py:405-465
# asked: {"lines": [406, 407, 410, 411, 412, 414, 415, 417, 418, 420, 422, 424, 425, 427, 430, 431, 432, 433, 434, 435, 436, 439, 440, 441, 442, 443, 444, 446, 448, 449, 450, 451, 452, 454, 455, 456, 457, 460, 462, 463, 465], "branches": [[410, 411], [410, 414], [414, 415], [414, 417], [417, 418], [417, 420], [424, 425], [424, 427], [448, 449], [448, 454], [454, 455], [454, 460]]}
# gained: {"lines": [406, 407, 410, 411, 412, 414, 415, 417, 418, 420, 422, 424, 427, 430, 431, 432, 433, 434, 435, 436, 439, 440, 441, 442, 446, 448, 449, 450, 451, 452, 454, 455, 456, 457, 460, 462, 463, 465], "branches": [[410, 411], [410, 414], [414, 415], [414, 417], [417, 418], [424, 427], [448, 449], [448, 454], [454, 455]]}

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)

def test_run_local_connection(action_module):
    action_module._connection.transport = 'local'
    action_module._task.action = 'reboot'
    result = action_module.run()
    assert result['changed'] is False
    assert result['elapsed'] == 0
    assert result['rebooted'] is False
    assert result['failed'] is True
    assert 'would reboot the control node' in result['msg']

def test_run_check_mode(action_module):
    action_module._play_context.check_mode = True
    result = action_module.run()
    assert result['changed'] is True
    assert result['elapsed'] == 0
    assert result['rebooted'] is True

def test_run_no_task_vars(action_module):
    action_module._play_context.check_mode = False
    action_module._connection.transport = 'ssh'
    with patch.object(ActionModule, 'deprecated_args') as mock_deprecated_args, \
         patch.object(ActionModule, 'get_distribution', return_value={'name': 'ubuntu'}), \
         patch.object(ActionModule, 'get_system_boot_time', return_value='boot_time'), \
         patch.object(ActionModule, 'perform_reboot', return_value={'failed': False, 'start': datetime.utcnow()}), \
         patch.object(ActionModule, 'validate_reboot', return_value={'rebooted': True, 'changed': True}):
        result = action_module.run()
        mock_deprecated_args.assert_called_once()
        assert result['rebooted'] is True
        assert result['changed'] is True
        assert 'elapsed' in result

def test_run_reboot_failure(action_module):
    action_module._play_context.check_mode = False
    action_module._connection.transport = 'ssh'
    with patch.object(ActionModule, 'deprecated_args'), \
         patch.object(ActionModule, 'get_distribution', return_value={'name': 'ubuntu'}), \
         patch.object(ActionModule, 'get_system_boot_time', return_value='boot_time'), \
         patch.object(ActionModule, 'perform_reboot', return_value={'failed': True, 'start': datetime.utcnow()}):
        result = action_module.run()
        assert result['failed'] is True
        assert 'elapsed' in result

def test_run_exception_handling(action_module):
    action_module._play_context.check_mode = False
    action_module._connection.transport = 'ssh'
    with patch.object(ActionModule, 'deprecated_args'), \
         patch.object(ActionModule, 'get_distribution', return_value={'name': 'ubuntu'}), \
         patch.object(ActionModule, 'get_system_boot_time', side_effect=Exception('error')):
        result = action_module.run()
        assert result['failed'] is True
        assert result['reboot'] is False
        assert 'error' in result['msg']
