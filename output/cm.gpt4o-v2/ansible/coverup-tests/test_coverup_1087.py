# file: lib/ansible/executor/process/worker.py:140-206
# asked: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 204, 206], "branches": [[190, 191], [190, 206]]}
# gained: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 204, 206], "branches": [[190, 191], [190, 206]]}

import pytest
from unittest.mock import Mock, patch
from ansible.executor.process.worker import WorkerProcess
from ansible.errors import AnsibleConnectionFailure
from jinja2.exceptions import TemplateNotFound
from ansible.executor.task_executor import TaskExecutor

@pytest.fixture
def worker_process():
    final_q = Mock()
    task_vars = Mock()
    host = Mock()
    task = Mock()
    play_context = Mock()
    loader = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker._new_stdin = Mock()  # Add this line to mock _new_stdin
    return worker

def test_run_task_executor_success(worker_process):
    with patch.object(TaskExecutor, 'run', return_value={'result': 'success'}) as mock_run:
        worker_process._run()
        assert worker_process._host.vars == {}
        assert worker_process._host.groups == []
        worker_process._final_q.send_task_result.assert_called_once_with(
            worker_process._host.name,
            worker_process._task._uuid,
            {'result': 'success'},
            task_fields=worker_process._task.dump_attrs()
        )
        mock_run.assert_called_once()

def test_run_task_executor_ansible_connection_failure(worker_process):
    with patch.object(TaskExecutor, 'run', side_effect=AnsibleConnectionFailure):
        worker_process._run()
        assert worker_process._host.vars == {}
        assert worker_process._host.groups == []
        worker_process._final_q.send_task_result.assert_called_once_with(
            worker_process._host.name,
            worker_process._task._uuid,
            {'unreachable': True},
            task_fields=worker_process._task.dump_attrs()
        )

def test_run_task_executor_generic_exception(worker_process):
    with patch.object(TaskExecutor, 'run', side_effect=Exception('generic error')):
        with patch('traceback.format_exc', return_value='traceback details'):
            worker_process._run()
            assert worker_process._host.vars == {}
            assert worker_process._host.groups == []
            worker_process._final_q.send_task_result.assert_called_once_with(
                worker_process._host.name,
                worker_process._task._uuid,
                {'failed': True, 'exception': 'traceback details', 'stdout': ''},
                task_fields=worker_process._task.dump_attrs()
            )

def test_run_task_executor_template_not_found_exception(worker_process):
    with patch.object(TaskExecutor, 'run', side_effect=TemplateNotFound('template not found')):
        with patch('traceback.format_exc', return_value='traceback details'):
            worker_process._run()
            assert worker_process._host.vars == {}
            assert worker_process._host.groups == []
            worker_process._final_q.send_task_result.assert_called_once_with(
                worker_process._host.name,
                worker_process._task._uuid,
                {'failed': True, 'exception': 'traceback details', 'stdout': ''},
                task_fields=worker_process._task.dump_attrs()
            )

def test_run_task_executor_io_error(worker_process):
    with patch.object(TaskExecutor, 'run', side_effect=IOError('io error')):
        worker_process._run()
        worker_process._final_q.send_task_result.assert_not_called()
