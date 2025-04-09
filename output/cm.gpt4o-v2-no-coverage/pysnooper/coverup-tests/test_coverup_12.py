# file: pysnooper/tracer.py:333-337
# asked: {"lines": [333, 334, 335, 336, 337], "branches": []}
# gained: {"lines": [333, 334, 335, 336, 337], "branches": []}

import pytest
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    tracer = Tracer()
    tracer.thread_info_padding = 0
    return tracer

def test_set_thread_info_padding_increase_padding(tracer):
    result = tracer.set_thread_info_padding("thread1")
    assert result == "thread1"
    assert tracer.thread_info_padding == 7

def test_set_thread_info_padding_no_increase(tracer):
    tracer.thread_info_padding = 10
    result = tracer.set_thread_info_padding("thread1")
    assert result == "thread1   "
    assert tracer.thread_info_padding == 10
