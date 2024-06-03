# file lib/ansible/executor/task_result.py:75-94
# lines [76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94]
# branches ['80->81', '80->83', '83->84', '83->85', '85->86', '85->87', '87->88', '87->89', '89->90', '89->91', '91->92', '91->94']

import pytest
from unittest.mock import Mock, patch

# Assuming the TaskResult class is imported from ansible.executor.task_result
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    host = Mock()
    task = Mock()
    return_data = "{}"  # Use a valid JSON string instead of a Mock object
    task_result = TaskResult(host=host, task=task, return_data=return_data)
    task_result._task_fields = {}
    return task_result

def test_needs_debugger_always(task_result):
    task_result._task_fields['debugger'] = 'always'
    assert task_result.needs_debugger() is True

def test_needs_debugger_never(task_result):
    task_result._task_fields['debugger'] = 'never'
    assert task_result.needs_debugger() is False

def test_needs_debugger_on_failed(task_result, mocker):
    task_result._task_fields['debugger'] = 'on_failed'
    mocker.patch.object(task_result, 'is_failed', return_value=True)
    mocker.patch.object(task_result, 'is_unreachable', return_value=False)
    assert task_result.needs_debugger() is True

def test_needs_debugger_on_unreachable(task_result, mocker):
    task_result._task_fields['debugger'] = 'on_unreachable'
    mocker.patch.object(task_result, 'is_failed', return_value=False)
    mocker.patch.object(task_result, 'is_unreachable', return_value=True)
    assert task_result.needs_debugger() is True

def test_needs_debugger_on_skipped(task_result, mocker):
    task_result._task_fields['debugger'] = 'on_skipped'
    mocker.patch.object(task_result, 'is_skipped', return_value=True)
    assert task_result.needs_debugger() is True

def test_needs_debugger_globally_enabled(task_result, mocker):
    task_result._task_fields['debugger'] = None
    mocker.patch.object(task_result, 'is_failed', return_value=True)
    mocker.patch.object(task_result, 'is_unreachable', return_value=False)
    with patch('ansible.executor.task_result.C.TASK_DEBUGGER_IGNORE_ERRORS', False):
        assert task_result.needs_debugger(globally_enabled=True) is True

def test_needs_debugger_ignore_errors(task_result, mocker):
    task_result._task_fields['debugger'] = None
    task_result._task_fields['ignore_errors'] = True
    mocker.patch.object(task_result, 'is_failed', return_value=True)
    mocker.patch.object(task_result, 'is_unreachable', return_value=False)
    with patch('ansible.executor.task_result.C.TASK_DEBUGGER_IGNORE_ERRORS', True):
        assert task_result.needs_debugger(globally_enabled=True) is False
