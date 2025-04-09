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
    thread_info = "Thread-1"
    padded_thread_info = tracer.set_thread_info_padding(thread_info)
    assert padded_thread_info == thread_info
    assert tracer.thread_info_padding == len(thread_info)

def test_set_thread_info_padding_increase(tracer):
    tracer.thread_info_padding = 5
    thread_info = "Thread-12345"
    padded_thread_info = tracer.set_thread_info_padding(thread_info)
    assert padded_thread_info == thread_info
    assert tracer.thread_info_padding == len(thread_info)

def test_set_thread_info_padding_no_change(tracer):
    tracer.thread_info_padding = 10
    thread_info = "Thread-1"
    padded_thread_info = tracer.set_thread_info_padding(thread_info)
    assert padded_thread_info == thread_info.ljust(10)
    assert tracer.thread_info_padding == 10
