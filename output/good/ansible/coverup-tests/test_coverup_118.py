# file lib/ansible/executor/task_result.py:75-94
# lines [75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94]
# branches ['80->81', '80->83', '83->84', '83->85', '85->86', '85->87', '87->88', '87->89', '89->90', '89->91', '91->92', '91->94']

import pytest
from ansible.executor.task_result import TaskResult
from ansible import constants as C
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def task_result(mocker):
    mock_host = mocker.Mock()
    mock_task = mocker.Mock()
    mock_data_loader = DataLoader()
    mock_return_data = mock_data_loader.load('{}')  # Mocking with a valid JSON string
    mock_task_result = TaskResult(mock_host, mock_task, mock_return_data)
    mock_task_result._task_fields = {}
    mock_task_result.is_failed = mocker.Mock(return_value=False)
    mock_task_result.is_unreachable = mocker.Mock(return_value=False)
    mock_task_result.is_skipped = mocker.Mock(return_value=False)
    return mock_task_result

def test_needs_debugger_always(task_result):
    task_result._task_fields['debugger'] = 'always'
    assert task_result.needs_debugger() is True

def test_needs_debugger_never(task_result):
    task_result._task_fields['debugger'] = 'never'
    assert task_result.needs_debugger() is False

def test_needs_debugger_on_failed(task_result):
    task_result._task_fields['debugger'] = 'on_failed'
    task_result.is_failed.return_value = True
    assert task_result.needs_debugger() is True

def test_needs_debugger_on_unreachable(task_result):
    task_result._task_fields['debugger'] = 'on_unreachable'
    task_result.is_unreachable.return_value = True
    assert task_result.needs_debugger() is True

def test_needs_debugger_on_skipped(task_result):
    task_result._task_fields['debugger'] = 'on_skipped'
    task_result.is_skipped.return_value = True
    assert task_result.needs_debugger() is True

def test_needs_debugger_globally_enabled_failed(task_result):
    task_result._task_fields['ignore_errors'] = False
    task_result.is_failed.return_value = True
    assert task_result.needs_debugger(globally_enabled=True) is True

def test_needs_debugger_globally_enabled_unreachable(task_result):
    task_result.is_unreachable.return_value = True
    assert task_result.needs_debugger(globally_enabled=True) is True

def test_needs_debugger_ignore_errors(task_result):
    task_result._task_fields['debugger'] = 'on_failed'
    task_result._task_fields['ignore_errors'] = True
    task_result.is_failed.return_value = True
    assert task_result.needs_debugger() is False

def test_needs_debugger_no_debugger_set(task_result):
    assert task_result.needs_debugger() is False
