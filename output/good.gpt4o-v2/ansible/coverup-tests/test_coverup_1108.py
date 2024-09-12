# file: lib/ansible/executor/task_result.py:75-94
# asked: {"lines": [76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94], "branches": [[80, 81], [80, 83], [83, 84], [83, 85], [85, 86], [85, 87], [87, 88], [87, 89], [89, 90], [89, 91], [91, 92], [91, 94]]}
# gained: {"lines": [76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94], "branches": [[80, 81], [80, 83], [83, 84], [83, 85], [85, 86], [85, 87], [87, 88], [87, 89], [89, 90], [89, 91], [91, 92], [91, 94]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible import constants as C

class MockTask:
    def __init__(self, debugger=None, ignore_errors=None):
        self._task_fields = {}
        if debugger is not None:
            self._task_fields['debugger'] = debugger
        if ignore_errors is not None:
            self._task_fields['ignore_errors'] = ignore_errors

@pytest.fixture
def mock_task_result():
    task = MockTask()
    return TaskResult(host=None, task=task, return_data={}, task_fields=task._task_fields)

def test_needs_debugger_always(mock_task_result):
    mock_task_result._task_fields['debugger'] = 'always'
    assert mock_task_result.needs_debugger() is True

def test_needs_debugger_never(mock_task_result):
    mock_task_result._task_fields['debugger'] = 'never'
    assert mock_task_result.needs_debugger() is False

def test_needs_debugger_on_failed(mock_task_result, monkeypatch):
    mock_task_result._task_fields['debugger'] = 'on_failed'
    monkeypatch.setattr(mock_task_result, 'is_failed', lambda: True)
    assert mock_task_result.needs_debugger() is True

def test_needs_debugger_on_unreachable(mock_task_result, monkeypatch):
    mock_task_result._task_fields['debugger'] = 'on_unreachable'
    monkeypatch.setattr(mock_task_result, 'is_unreachable', lambda: True)
    assert mock_task_result.needs_debugger() is True

def test_needs_debugger_on_skipped(mock_task_result, monkeypatch):
    mock_task_result._task_fields['debugger'] = 'on_skipped'
    monkeypatch.setattr(mock_task_result, 'is_skipped', lambda: True)
    assert mock_task_result.needs_debugger() is True

def test_needs_debugger_globally_enabled(mock_task_result, monkeypatch):
    monkeypatch.setattr(mock_task_result, 'is_failed', lambda: True)
    assert mock_task_result.needs_debugger(globally_enabled=True) is True

def test_needs_debugger_ignore_errors(mock_task_result, monkeypatch):
    mock_task_result._task_fields['ignore_errors'] = True
    monkeypatch.setattr(C, 'TASK_DEBUGGER_IGNORE_ERRORS', True)
    monkeypatch.setattr(mock_task_result, 'is_failed', lambda: True)
    assert mock_task_result.needs_debugger(globally_enabled=True) is False
