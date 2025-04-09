# file: lib/ansible/plugins/callback/junit.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.plugins.callback import CallbackBase
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_no_hosts(callback_module, mocker):
    task_mock = Mock()
    start_task_spy = mocker.spy(callback_module, '_start_task')
    
    callback_module.v2_runner_on_no_hosts(task_mock)
    
    start_task_spy.assert_called_once_with(task_mock)
