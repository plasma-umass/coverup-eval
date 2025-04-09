# file: pysnooper/tracer.py:333-337
# asked: {"lines": [333, 334, 335, 336, 337], "branches": []}
# gained: {"lines": [333, 334, 335, 336, 337], "branches": []}

import pytest
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    return Tracer()

def test_set_thread_info_padding_initial(tracer):
    tracer.thread_info_padding = 0
    result = tracer.set_thread_info_padding("thread1")
    assert result == "thread1"
    assert tracer.thread_info_padding == 7

def test_set_thread_info_padding_increase(tracer):
    tracer.thread_info_padding = 5
    result = tracer.set_thread_info_padding("longer_thread")
    assert result == "longer_thread"
    assert tracer.thread_info_padding == 13

def test_set_thread_info_padding_no_change(tracer):
    tracer.thread_info_padding = 15
    result = tracer.set_thread_info_padding("short")
    assert result == "short          "
    assert tracer.thread_info_padding == 15
