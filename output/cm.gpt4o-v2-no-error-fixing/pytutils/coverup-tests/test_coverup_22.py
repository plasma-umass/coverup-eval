# file: pytutils/log.py:24-34
# asked: {"lines": [24, 34], "branches": []}
# gained: {"lines": [24, 34], "branches": []}

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(monkeypatch):
    # Mock inspect.stack to control the call stack
    class MockFrame:
        def __init__(self, f_globals):
            self.f_globals = f_globals

    def mock_stack():
        return [
            None,  # Current frame
            None,  # Caller frame
            [MockFrame({'__name__': 'test_module'})]  # Caller's caller frame
        ]

    monkeypatch.setattr(inspect, 'stack', mock_stack)

    # Call the function and assert the expected result
    result = _namespace_from_calling_context()
    assert result == 'test_module'
