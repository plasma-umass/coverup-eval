# file: pysnooper/tracer.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from pysnooper.tracer import Tracer

def test_is_internal_frame(monkeypatch):
    tracer = Tracer()

    class MockFrame:
        f_code = type('code', (object,), {'co_filename': Tracer.__enter__.__code__.co_filename})

    frame = MockFrame()
    assert tracer._is_internal_frame(frame) == True

    class MockFrameDifferentFile:
        f_code = type('code', (object,), {'co_filename': 'different_file.py'})

    frame_different = MockFrameDifferentFile()
    assert tracer._is_internal_frame(frame_different) == False
