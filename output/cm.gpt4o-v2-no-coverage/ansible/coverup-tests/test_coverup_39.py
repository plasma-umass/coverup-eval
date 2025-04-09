# file: lib/ansible/executor/process/worker.py:140-206
# asked: {"lines": [140, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 204, 206], "branches": [[190, 191], [190, 206]]}
# gained: {"lines": [140, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 204, 206], "branches": [[190, 191], [190, 206]]}

import pytest
from unittest.mock import Mock, patch
from ansible.executor.process.worker import WorkerProcess
from ansible.errors import AnsibleConnectionFailure
from jinja2.exceptions import TemplateNotFound

@pytest.fixture
def mock_worker_process():
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

def test_run_task_executor_success(mock_worker_process):
    with patch('ansible.executor.task_executor.TaskExecutor.run', return_value={'result': 'success'}):
        mock_worker_process._run()
        mock_worker_process._final_q.send_task_result.assert_called_once_with(
            mock_worker_process._host.name,
            mock_worker_process._task._uuid,
            {'result': 'success'},
            task_fields=mock_worker_process._task.dump_attrs()
        )
        assert mock_worker_process._host.vars == {}
        assert mock_worker_process._host.groups == []

def test_run_task_executor_ansible_connection_failure(mock_worker_process):
    with patch('ansible.executor.task_executor.TaskExecutor.run', side_effect=AnsibleConnectionFailure):
        mock_worker_process._run()
        mock_worker_process._final_q.send_task_result.assert_called_once_with(
            mock_worker_process._host.name,
            mock_worker_process._task._uuid,
            {'unreachable': True},
            task_fields=mock_worker_process._task.dump_attrs()
        )
        assert mock_worker_process._host.vars == {}
        assert mock_worker_process._host.groups == []

def test_run_task_executor_generic_exception(mock_worker_process):
    with patch('ansible.executor.task_executor.TaskExecutor.run', side_effect=Exception('generic error')):
        with patch('traceback.format_exc', return_value='traceback details'):
            mock_worker_process._run()
            mock_worker_process._final_q.send_task_result.assert_called_once_with(
                mock_worker_process._host.name,
                mock_worker_process._task._uuid,
                {'failed': True, 'exception': 'traceback details', 'stdout': ''},
                task_fields=mock_worker_process._task.dump_attrs()
            )
            assert mock_worker_process._host.vars == {}
            assert mock_worker_process._host.groups == []

def test_run_task_executor_ioerror_exception(mock_worker_process):
    with patch('ansible.executor.task_executor.TaskExecutor.run', side_effect=IOError('IO error')):
        mock_worker_process._run()
        mock_worker_process._final_q.send_task_result.assert_not_called()

def test_run_task_executor_template_not_found_exception(mock_worker_process):
    with patch('ansible.executor.task_executor.TaskExecutor.run', side_effect=TemplateNotFound('template not found')):
        with patch('traceback.format_exc', return_value='traceback details'):
            mock_worker_process._run()
            mock_worker_process._final_q.send_task_result.assert_called_once_with(
                mock_worker_process._host.name,
                mock_worker_process._task._uuid,
                {'failed': True, 'exception': 'traceback details', 'stdout': ''},
                task_fields=mock_worker_process._task.dump_attrs()
            )
            assert mock_worker_process._host.vars == {}
            assert mock_worker_process._host.groups == []
