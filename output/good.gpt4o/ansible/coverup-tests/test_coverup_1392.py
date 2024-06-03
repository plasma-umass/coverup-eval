# file lib/ansible/plugins/callback/junit.py:255-274
# lines [258, 260, 261, 262, 264, 265, 267, 268, 269, 271, 273, 274]
# branches ['260->261', '260->267', '261->262', '261->264', '264->260', '264->265']

import os
import time
import pytest
from unittest.mock import MagicMock, patch, mock_open
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._task_data = {
        'task_uuid_1': MagicMock(action='setup', host_data={'host_uuid_1': MagicMock()}),
        'task_uuid_2': MagicMock(action='other_action', host_data={'host_uuid_2': MagicMock()})
    }
    module._include_setup_tasks_in_report = 'false'
    module._playbook_name = 'test_playbook'
    module._output_dir = '/tmp'
    return module

def test_generate_report(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.junit.TestSuite', autospec=True)
    mocker.patch('ansible.plugins.callback.junit.TestSuites', autospec=True)
    mocker.patch('ansible.plugins.callback.junit.to_bytes', return_value=b'<xml>report</xml>')
    mocker.patch('os.path.join', return_value='/tmp/test_playbook-1234567890.xml')
    mocker.patch('time.time', return_value=1234567890)
    mock_open_func = mock_open()
    mocker.patch('builtins.open', mock_open_func)

    callback_module._build_test_case = MagicMock(return_value='test_case')
    
    callback_module._generate_report()

    callback_module._build_test_case.assert_called_once_with(
        callback_module._task_data['task_uuid_2'], 
        callback_module._task_data['task_uuid_2'].host_data['host_uuid_2']
    )
    mock_open_func.assert_called_once_with('/tmp/test_playbook-1234567890.xml', 'wb')
    mock_open_func().write.assert_called_once_with(b'<xml>report</xml>')
