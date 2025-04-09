# file: lib/ansible/plugins/callback/default.py:290-304
# asked: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292], [291, 294]]}
# gained: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module(mocker):
    module = CallbackModule()
    module._display = Mock()
    module._display.verbosity = 2
    return module

def test_v2_runner_item_on_failed(callback_module, mocker):
    result = Mock()
    result._task._uuid = "1234"
    result._task.no_log = False
    result._task.action = "test_action"
    result._task.delegate_to = None
    result._host.get_name.return_value = "localhost"
    result._result = {
        '_ansible_verbose_always': True,
        '_ansible_item_label': 'item_label',
        'warnings': ['warning1'],
        'deprecations': [{'msg': 'deprecated', 'version': '2.0'}],
        'exception': 'Traceback (most recent call last):\nError'
    }

    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value="localhost")
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_get_item_label', return_value="item_label")
    mocker.patch.object(callback_module, '_dump_results', return_value="dumped_results")

    callback_module._last_task_banner = "5678"
    callback_module.display_failed_stderr = True

    callback_module.v2_runner_item_on_failed(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module.host_label.assert_called_once_with(result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=item_label) => dumped_results",
        color=C.COLOR_ERROR,
        stderr=True
    )
