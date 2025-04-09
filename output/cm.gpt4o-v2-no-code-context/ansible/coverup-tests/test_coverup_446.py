# file: lib/ansible/plugins/callback/default.py:422-430
# asked: {"lines": [422, 423, 427, 428, 429, 430], "branches": [[428, 429], [428, 430]]}
# gained: {"lines": [422, 423, 427, 428, 429, 430], "branches": [[428, 429], [428, 430]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_async_failed_with_jid(callback_module, mocker):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {'ansible_job_id': '12345'}
    
    display_mock = mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_async_failed(result)
    
    display_mock.assert_called_once_with("ASYNC FAILED on test_host: jid=12345", color=mocker.ANY)

def test_v2_runner_on_async_failed_without_jid_with_async_result(callback_module, mocker):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {'async_result': {'ansible_job_id': '67890'}}
    
    display_mock = mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_async_failed(result)
    
    display_mock.assert_called_once_with("ASYNC FAILED on test_host: jid=67890", color=mocker.ANY)

def test_v2_runner_on_async_failed_without_jid_and_async_result(callback_module, mocker):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {}
    
    display_mock = mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_async_failed(result)
    
    display_mock.assert_called_once_with("ASYNC FAILED on test_host: jid=None", color=mocker.ANY)
