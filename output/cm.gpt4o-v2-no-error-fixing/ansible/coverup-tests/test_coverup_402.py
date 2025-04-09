# file: lib/ansible/plugins/callback/junit.py:295-299
# asked: {"lines": [295, 296, 297, 299], "branches": [[296, 297], [296, 299]]}
# gained: {"lines": [295, 296, 297, 299], "branches": [[296, 297], [296, 299]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_failed_ignore_errors(callback_module, mocker):
    result = MagicMock()
    mocker.patch.object(callback_module, '_finish_task')

    callback_module._fail_on_ignore = 'false'
    callback_module.v2_runner_on_failed(result, ignore_errors=True)

    callback_module._finish_task.assert_called_once_with('ok', result)

def test_v2_runner_on_failed_no_ignore_errors(callback_module, mocker):
    result = MagicMock()
    mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_failed(result, ignore_errors=False)

    callback_module._finish_task.assert_called_once_with('failed', result)

def test_v2_runner_on_failed_ignore_errors_fail_on_ignore_true(callback_module, mocker):
    result = MagicMock()
    mocker.patch.object(callback_module, '_finish_task')

    callback_module._fail_on_ignore = 'true'
    callback_module.v2_runner_on_failed(result, ignore_errors=True)

    callback_module._finish_task.assert_called_once_with('failed', result)
