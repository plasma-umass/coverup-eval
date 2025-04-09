# file: lib/ansible/plugins/callback/default.py:399-405
# asked: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}
# gained: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.color import C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_retry(callback_module, monkeypatch):
    # Mocking the result object
    result = MagicMock()
    result.task_name = "test_task"
    result._task = "test_task"
    result._result = {'retries': 3, 'attempts': 1}
    
    # Mocking the host_label method
    monkeypatch.setattr(callback_module, 'host_label', lambda x: "test_host")
    
    # Mocking the _run_is_verbose method
    monkeypatch.setattr(callback_module, '_run_is_verbose', lambda x, verbosity: True)
    
    # Mocking the _dump_results method
    monkeypatch.setattr(callback_module, '_dump_results', lambda x: "dumped_result")
    
    # Mocking the _display.display method
    display_mock = MagicMock()
    monkeypatch.setattr(callback_module, '_display', display_mock)
    
    # Call the method
    callback_module.v2_runner_retry(result)
    
    # Assertions
    expected_msg = "FAILED - RETRYING: [test_host]: test_task (2 retries left).Result was: dumped_result"
    display_mock.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)

def test_v2_runner_retry_non_verbose(callback_module, monkeypatch):
    # Mocking the result object
    result = MagicMock()
    result.task_name = "test_task"
    result._task = "test_task"
    result._result = {'retries': 3, 'attempts': 1}
    
    # Mocking the host_label method
    monkeypatch.setattr(callback_module, 'host_label', lambda x: "test_host")
    
    # Mocking the _run_is_verbose method
    monkeypatch.setattr(callback_module, '_run_is_verbose', lambda x, verbosity: False)
    
    # Mocking the _display.display method
    display_mock = MagicMock()
    monkeypatch.setattr(callback_module, '_display', display_mock)
    
    # Call the method
    callback_module.v2_runner_retry(result)
    
    # Assertions
    expected_msg = "FAILED - RETRYING: [test_host]: test_task (2 retries left)."
    display_mock.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)
