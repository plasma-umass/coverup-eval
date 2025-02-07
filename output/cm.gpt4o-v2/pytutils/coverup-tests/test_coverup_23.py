# file: pytutils/log.py:24-34
# asked: {"lines": [24, 34], "branches": []}
# gained: {"lines": [24, 34], "branches": []}

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(monkeypatch):
    # Mock inspect.stack to control the calling context
    class MockFrame:
        f_globals = {"__name__": "mocked.module"}

    def mock_stack():
        return [None, None, [MockFrame()]]

    monkeypatch.setattr(inspect, 'stack', mock_stack)

    # Call the function and assert the expected result
    result = _namespace_from_calling_context()
    assert result == "mocked.module"
