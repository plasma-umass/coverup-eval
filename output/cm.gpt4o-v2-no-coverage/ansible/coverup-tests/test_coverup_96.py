# file: lib/ansible/executor/task_result.py:75-94
# asked: {"lines": [75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94], "branches": [[80, 81], [80, 83], [83, 84], [83, 85], [85, 86], [85, 87], [87, 88], [87, 89], [89, 90], [89, 91], [91, 92], [91, 94]]}
# gained: {"lines": [75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94], "branches": [[80, 81], [80, 83], [83, 84], [83, 85], [85, 86], [85, 87], [87, 88], [87, 89], [89, 90], [89, 91], [91, 92], [91, 94]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible import constants as C

@pytest.fixture
def task_result():
    class MockTaskResult(TaskResult):
        def __init__(self, task_fields, result):
            self._task_fields = task_fields
            self._result = result

        def _check_key(self, key):
            return self._result.get(key, False)

    return MockTaskResult

def test_needs_debugger_always(task_result):
    tr = task_result({'debugger': 'always'}, {})
    assert tr.needs_debugger() is True

def test_needs_debugger_never(task_result):
    tr = task_result({'debugger': 'never'}, {})
    assert tr.needs_debugger() is False

def test_needs_debugger_on_failed(task_result):
    tr = task_result({'debugger': 'on_failed'}, {'failed': True})
    assert tr.needs_debugger() is True

def test_needs_debugger_on_unreachable(task_result):
    tr = task_result({'debugger': 'on_unreachable'}, {'unreachable': True})
    assert tr.needs_debugger() is True

def test_needs_debugger_on_skipped(task_result):
    tr = task_result({'debugger': 'on_skipped'}, {'skipped': True})
    assert tr.needs_debugger() is True

def test_needs_debugger_globally_enabled(task_result, monkeypatch):
    monkeypatch.setattr(C, 'TASK_DEBUGGER_IGNORE_ERRORS', False)
    tr = task_result({}, {'failed': True})
    assert tr.needs_debugger(globally_enabled=True) is True

def test_needs_debugger_globally_enabled_ignore_errors(task_result, monkeypatch):
    monkeypatch.setattr(C, 'TASK_DEBUGGER_IGNORE_ERRORS', True)
    tr = task_result({'ignore_errors': True}, {'failed': True})
    assert tr.needs_debugger(globally_enabled=True) is False

def test_needs_debugger_globally_enabled_unreachable(task_result):
    tr = task_result({}, {'unreachable': True})
    assert tr.needs_debugger(globally_enabled=True) is True
