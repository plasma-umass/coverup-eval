# file: pytutils/log.py:24-34
# asked: {"lines": [24, 34], "branches": []}
# gained: {"lines": [24, 34], "branches": []}

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(monkeypatch):
    def mock_stack():
        class Frame:
            f_globals = {"__name__": "mocked.module"}
        
        class FrameInfo:
            def __getitem__(self, item):
                if item == 0:
                    return Frame()
                raise IndexError("Invalid index")
        
        return [None, None, FrameInfo()]
    
    monkeypatch.setattr(inspect, 'stack', mock_stack)
    
    result = _namespace_from_calling_context()
    assert result == "mocked.module"
