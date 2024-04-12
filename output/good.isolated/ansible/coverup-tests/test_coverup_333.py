# file lib/ansible/plugins/callback/default.py:290-304
# lines [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303]
# branches ['291->292', '291->294']

import pytest
from ansible.plugins.callback import default
from unittest.mock import MagicMock, patch

# Mocking the required Ansible classes and methods
class FakeTask:
    def __init__(self, uuid):
        self._uuid = uuid
        self.action = 'fake_action'
        self.delegate_to = None

class FakeResult:
    def __init__(self, task_uuid):
        self._task = FakeTask(task_uuid)
        self._result = {
            'failed': True,
            'msg': 'Some failure message',
            'item': 'some_item'
        }
        self._host = MagicMock()
        self._host.name = 'localhost'
        self._host.get_name = MagicMock(return_value='localhost')

@pytest.fixture
def callback_module():
    return default.CallbackModule()

@pytest.fixture
def task_result():
    return FakeResult(task_uuid='1234')

def test_v2_runner_item_on_failed(callback_module, task_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_get_item_label', return_value='some_item_label')
    mocker.patch.object(callback_module, '_dump_results', return_value='some_dumped_results')
    mocker.patch.object(callback_module._display, 'display')

    callback_module._last_task_banner = None
    callback_module.display_failed_stderr = False

    callback_module.v2_runner_item_on_failed(task_result)

    callback_module._print_task_banner.assert_called_once_with(task_result._task)
    callback_module._clean_results.assert_called_once_with(task_result._result, task_result._task.action)
    callback_module._handle_exception.assert_called_once_with(task_result._result, use_stderr=False)
    callback_module._handle_warnings.assert_called_once_with(task_result._result)
    callback_module._get_item_label.assert_called_once_with(task_result._result)
    callback_module._dump_results.assert_called_once_with(task_result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=some_item_label) => some_dumped_results",
        color=default.C.COLOR_ERROR,
        stderr=False
    )
