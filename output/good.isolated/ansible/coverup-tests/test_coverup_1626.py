# file lib/ansible/plugins/callback/default.py:422-430
# lines [423, 427, 428, 429, 430]
# branches ['428->429', '428->430']

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

@pytest.fixture
def callback_module():
    return default.CallbackModule()

@pytest.fixture
def task_result(mocker):
    fake_loader = DataLoader()
    inventory = InventoryManager(loader=fake_loader)
    host = Host(name='testhost')
    inventory.add_host(host.name)
    result = TaskResult(
        host=host,
        task=mocker.MagicMock(),
        return_data={
            'failed': True,
            'msg': 'Async task did not complete within the requested time',
            'async_result': {'ansible_job_id': '12345'}
        }
    )
    return result

def test_v2_runner_on_async_failed_with_async_result(callback_module, task_result, mocker):
    display_mock = mocker.patch.object(callback_module._display, 'display')
    callback_module.v2_runner_on_async_failed(task_result)
    display_mock.assert_called_once_with("ASYNC FAILED on testhost: jid=12345", color=default.C.COLOR_DEBUG)
