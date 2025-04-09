# file: pytutils/log.py:24-34
# asked: {"lines": [24, 34], "branches": []}
# gained: {"lines": [24, 34], "branches": []}

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(monkeypatch):
    def mock_stack():
        class MockFrame:
            f_globals = {"__name__": "mocked.module"}
        
        return [None, None, (MockFrame(),)]
    
    monkeypatch.setattr(inspect, 'stack', mock_stack)
    
    result = _namespace_from_calling_context()
    assert result == "mocked.module"
