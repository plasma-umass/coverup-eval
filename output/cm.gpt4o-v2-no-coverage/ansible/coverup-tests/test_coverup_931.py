# file: lib/ansible/plugins/callback/junit.py:289-290
# asked: {"lines": [289, 290], "branches": []}
# gained: {"lines": [289, 290], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

class TestCallbackModule:
    
    @pytest.fixture
    def callback_module(self):
        return CallbackModule()

    def test_v2_playbook_on_cleanup_task_start(self, callback_module, mocker):
        task_mock = Mock()
        start_task_spy = mocker.spy(callback_module, '_start_task')
        
        callback_module.v2_playbook_on_cleanup_task_start(task_mock)
        
        start_task_spy.assert_called_once_with(task_mock)
