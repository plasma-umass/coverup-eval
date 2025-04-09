# file: pysnooper/tracer.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from unittest.mock import MagicMock
from pysnooper.tracer import Tracer

def test_is_internal_frame():
    tracer = Tracer()
    frame = MagicMock()
    frame.f_code.co_filename = Tracer.__enter__.__code__.co_filename
    assert tracer._is_internal_frame(frame) == True

    frame.f_code.co_filename = "some_other_file.py"
    assert tracer._is_internal_frame(frame) == False
