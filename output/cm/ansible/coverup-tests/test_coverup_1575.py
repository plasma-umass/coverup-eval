# file lib/ansible/plugins/callback/oneline.py:58-71
# lines [60, 61, 62, 64, 65, 67, 68, 70, 71]
# branches ['60->61', '60->64', '67->68', '67->70']

import pytest
from ansible.plugins.callback.oneline import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.utils.color import stringc
from unittest.mock import MagicMock

@pytest.fixture
def oneline_callback():
    return CallbackModule()

@pytest.fixture
def task_result(mocker):
    fake_result = TaskResult(
        host=mocker.MagicMock(),
        task=mocker.MagicMock(),
        return_data={
            'changed': True,
            'ansible_job_id': '1234'
        }
    )
    fake_result._host.get_name.return_value = 'testhost'
    fake_result._task.action = 'fake_action'
    return fake_result

def test_v2_runner_on_ok_changed_with_ansible_job_id(oneline_callback, task_result, mocker):
    mocker.patch('ansible.plugins.callback.oneline.C.COLOR_CHANGED', 'yellow')
    mocker.patch('ansible.plugins.callback.oneline.C.COLOR_OK', 'green')
    mocker.patch('ansible.plugins.callback.oneline.C.MODULE_NO_JSON', [])
    display_mock = mocker.MagicMock()
    oneline_callback._display = display_mock
    oneline_callback._dump_results = mocker.MagicMock(return_value='{}')

    oneline_callback.v2_runner_on_ok(task_result)

    display_mock.display.assert_called_once_with(
        'testhost | CHANGED => {}',
        color='yellow'
    )
