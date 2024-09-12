# file: pysnooper/tracer.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
import types
from pysnooper.tracer import Tracer

@pytest.fixture
def mock_frame():
    frame = types.SimpleNamespace()
    frame.f_code = types.SimpleNamespace()
    return frame

def test_is_internal_frame_true(mock_frame, monkeypatch):
    mock_frame.f_code.co_filename = Tracer.__enter__.__code__.co_filename
    tracer = Tracer()
    assert tracer._is_internal_frame(mock_frame) is True

def test_is_internal_frame_false(mock_frame, monkeypatch):
    mock_frame.f_code.co_filename = "some_other_file.py"
    tracer = Tracer()
    assert tracer._is_internal_frame(mock_frame) is False
