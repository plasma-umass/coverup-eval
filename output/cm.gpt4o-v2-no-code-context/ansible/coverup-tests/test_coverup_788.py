# file: lib/ansible/plugins/callback/default.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task import Task

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module, mocker):
    task = mocker.Mock(spec=Task)
    mock_task_start = mocker.patch.object(callback_module, '_task_start')

    callback_module.v2_playbook_on_handler_task_start(task)

    mock_task_start.assert_called_once_with(task, prefix='RUNNING HANDLER')
