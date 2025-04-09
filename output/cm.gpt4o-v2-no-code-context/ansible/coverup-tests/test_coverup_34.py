# file: lib/ansible/executor/process/worker.py:140-206
# asked: {"lines": [140, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 204, 206], "branches": [[190, 191], [190, 206]]}
# gained: {"lines": [140, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 204, 206], "branches": [[190, 191]]}

import pytest
from unittest.mock import Mock, patch, create_autospec
from ansible.executor.process.worker import WorkerProcess
from ansible.executor.task_executor import TaskExecutor
from ansible.errors import AnsibleConnectionFailure
from jinja2 import TemplateNotFound
import traceback

@pytest.fixture
def worker_process():
    worker = WorkerProcess(
        final_q=Mock(),
        task_vars=Mock(),
        host=Mock(),
        task=Mock(),
        play_context=Mock(),
        loader=Mock(),
        variable_manager=Mock(),
        shared_loader_obj=Mock()
    )
    worker._new_stdin = Mock()  # Add this line to avoid the AttributeError
    return worker

def test_run_success(worker_process, mocker):
    mocker.patch.object(TaskExecutor, 'run', return_value='executor_result')
    worker_process._task._uuid = 'test_uuid'
    worker_process._task.dump_attrs = Mock(return_value='task_attrs')

    worker_process._run()

    worker_process._final_q.send_task_result.assert_called_once_with(
        worker_process._host.name,
        'test_uuid',
        'executor_result',
        task_fields='task_attrs'
    )
    assert worker_process._host.vars == {}
    assert worker_process._host.groups == []

def test_run_ansible_connection_failure(worker_process, mocker):
    mocker.patch.object(TaskExecutor, 'run', side_effect=AnsibleConnectionFailure)
    worker_process._task._uuid = 'test_uuid'
    worker_process._task.dump_attrs = Mock(return_value='task_attrs')

    worker_process._run()

    worker_process._final_q.send_task_result.assert_called_once_with(
        worker_process._host.name,
        'test_uuid',
        {'unreachable': True},
        task_fields='task_attrs'
    )
    assert worker_process._host.vars == {}
    assert worker_process._host.groups == []

def test_run_generic_exception(worker_process, mocker):
    mocker.patch.object(TaskExecutor, 'run', side_effect=Exception('test_exception'))
    worker_process._task._uuid = 'test_uuid'
    worker_process._task.dump_attrs = Mock(return_value='task_attrs')
    mocker.patch('traceback.format_exc', return_value='traceback_info')
    mocker.patch.object(worker_process, '_clean_up')

    worker_process._run()

    worker_process._final_q.send_task_result.assert_called_once_with(
        worker_process._host.name,
        'test_uuid',
        {'failed': True, 'exception': 'traceback_info', 'stdout': ''},
        task_fields='task_attrs'
    )
    worker_process._clean_up.assert_called_once()
    assert worker_process._host.vars == {}
    assert worker_process._host.groups == []

def test_run_template_not_found_exception(worker_process, mocker):
    mocker.patch.object(TaskExecutor, 'run', side_effect=TemplateNotFound('template_not_found'))
    worker_process._task._uuid = 'test_uuid'
    worker_process._task.dump_attrs = Mock(return_value='task_attrs')
    mocker.patch('traceback.format_exc', return_value='traceback_info')
    mocker.patch.object(worker_process, '_clean_up')

    worker_process._run()

    worker_process._final_q.send_task_result.assert_called_once_with(
        worker_process._host.name,
        'test_uuid',
        {'failed': True, 'exception': 'traceback_info', 'stdout': ''},
        task_fields='task_attrs'
    )
    worker_process._clean_up.assert_called_once()
    assert worker_process._host.vars == {}
    assert worker_process._host.groups == []
