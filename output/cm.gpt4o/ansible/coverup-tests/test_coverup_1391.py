# file lib/ansible/plugins/callback/default.py:78-99
# lines [80, 81, 83, 84, 86, 87, 89, 90, 93, 94, 95, 96, 98, 99]
# branches ['83->84', '83->86', '89->90', '89->93', '93->94', '93->95', '98->exit', '98->99']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_failed_stderr = True  # Mock the missing attribute
    return module

@pytest.fixture
def result():
    result = MagicMock()
    result._result = {'msg': 'An error occurred'}
    result._task.action = 'some_action'
    result._task._uuid = 'unique-task-uuid'
    result._task.loop = False
    return result

def test_v2_runner_on_failed(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_print_task_path')
    mocker.patch.object(callback_module, '_dump_results', return_value='{"msg": "An error occurred"}')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, 'get_option', return_value=True)

    # Set _last_task_banner to a different value to trigger the banner print
    callback_module._last_task_banner = 'different-uuid'

    # Call the method with ignore_errors=False
    callback_module.v2_runner_on_failed(result, ignore_errors=False)

    # Assertions to verify the correct methods were called
    callback_module.host_label.assert_called_once_with(result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._dump_results.assert_called_once_with(result._result)
    callback_module._display.display.assert_any_call('fatal: [localhost]: FAILED! => {"msg": "An error occurred"}', color=mocker.ANY, stderr=callback_module.display_failed_stderr)
    callback_module._print_task_path.assert_called_once_with(result._task)

    # Call the method with ignore_errors=True
    callback_module.v2_runner_on_failed(result, ignore_errors=True)

    # Verify the ignore_errors message is displayed
    callback_module._display.display.assert_any_call("...ignoring", color=mocker.ANY)
