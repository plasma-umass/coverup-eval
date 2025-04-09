# file: lib/ansible/plugins/callback/oneline.py:58-71
# asked: {"lines": [58, 60, 61, 62, 64, 65, 67, 68, 70, 71], "branches": [[60, 61], [60, 64], [67, 68], [67, 70]]}
# gained: {"lines": [58, 60, 61, 62, 64, 65, 67, 68, 70, 71], "branches": [[60, 61], [60, 64], [67, 68], [67, 70]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def result():
    mock_result = Mock()
    mock_result._result = {}
    mock_result._task = Mock()
    mock_result._host = Mock()
    mock_result._host.get_name.return_value = 'localhost'
    return mock_result

def test_v2_runner_on_ok_changed(callback_module, result):
    result._result['changed'] = True
    result._task.action = 'some_action'
    
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_ok(result)
        mock_display.assert_called_once()
        assert 'CHANGED' in mock_display.call_args[0][0]

def test_v2_runner_on_ok_success(callback_module, result):
    result._result['changed'] = False
    result._task.action = 'some_action'
    
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_ok(result)
        mock_display.assert_called_once()
        assert 'SUCCESS' in mock_display.call_args[0][0]

def test_v2_runner_on_ok_no_json(callback_module, result):
    result._result['changed'] = False
    result._task.action = C.MODULE_NO_JSON[0]
    
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_ok(result)
        mock_display.assert_called_once()
        assert 'SUCCESS' in mock_display.call_args[0][0]

def test_v2_runner_on_ok_with_ansible_job_id(callback_module, result):
    result._result['changed'] = False
    result._result['ansible_job_id'] = '12345'
    result._task.action = C.MODULE_NO_JSON[0]
    
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_ok(result)
        mock_display.assert_called_once()
        assert 'SUCCESS' in mock_display.call_args[0][0]
