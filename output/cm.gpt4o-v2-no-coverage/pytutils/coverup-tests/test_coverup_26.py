# file: pytutils/log.py:24-34
# asked: {"lines": [24, 34], "branches": []}
# gained: {"lines": [24, 34], "branches": []}

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(monkeypatch):
    # Mock inspect.stack to control the calling context
    class MockFrame:
        def __init__(self, f_globals):
            self.f_globals = f_globals

    class MockFrameInfo:
        def __init__(self, frame):
            self.frame = frame

        def __getitem__(self, item):
            if item == 0:
                return self.frame
            raise IndexError("MockFrameInfo only supports index 0")

    def mock_stack():
        mock_globals = {'__name__': 'mocked.module'}
        mock_frame = MockFrame(mock_globals)
        mock_frame_info = MockFrameInfo(mock_frame)
        return [None, None, mock_frame_info]

    monkeypatch.setattr(inspect, 'stack', mock_stack)

    result = _namespace_from_calling_context()
    assert result == 'mocked.module'
