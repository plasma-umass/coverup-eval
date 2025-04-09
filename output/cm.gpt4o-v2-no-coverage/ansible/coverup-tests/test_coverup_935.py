# file: lib/ansible/plugins/callback/junit.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

class TestCallbackModule:
    
    @pytest.fixture
    def callback_module(self):
        return CallbackModule()
    
    def test_v2_runner_on_no_hosts(self, callback_module, mocker):
        task_mock = Mock()
        start_task_spy = mocker.spy(callback_module, '_start_task')
        
        callback_module.v2_runner_on_no_hosts(task_mock)
        
        start_task_spy.assert_called_once_with(task_mock)
    
    def test_start_task(self, callback_module):
        task_mock = Mock()
        task_mock._uuid = '1234'
        task_mock.get_name.return_value = 'test_task'
        task_mock.get_path.return_value = '/path/to/task'
        task_mock.action = 'test_action'
        task_mock.no_log = False
        task_mock.args = {'arg1': 'value1', 'arg2': 'value2'}
        
        callback_module._task_data = {}
        callback_module._play_name = 'test_play'
        callback_module._hide_task_arguments = 'false'
        
        callback_module._start_task(task_mock)
        
        assert '1234' in callback_module._task_data
        task_data = callback_module._task_data['1234']
        assert task_data.uuid == '1234'
        assert task_data.name == 'test_task arg1=value1, arg2=value2'
        assert task_data.path == '/path/to/task'
        assert task_data.play == 'test_play'
        assert task_data.action == 'test_action'
