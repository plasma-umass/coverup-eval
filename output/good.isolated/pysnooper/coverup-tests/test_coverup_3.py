# file pysnooper/tracer.py:333-337
# lines [333, 334, 335, 336, 337]
# branches []

import pytest
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    return Tracer()

def test_set_thread_info_padding(tracer):
    initial_thread_info = 'Thread-1'
    longer_thread_info = 'LongerThread-2'

    # Test with initial thread info
    padded_thread_info = tracer.set_thread_info_padding(initial_thread_info)
    assert padded_thread_info == initial_thread_info.ljust(len(initial_thread_info))
    assert tracer.thread_info_padding == len(initial_thread_info)

    # Test with longer thread info to ensure padding is updated
    padded_longer_thread_info = tracer.set_thread_info_padding(longer_thread_info)
    assert padded_longer_thread_info == longer_thread_info.ljust(len(longer_thread_info))
    assert tracer.thread_info_padding == len(longer_thread_info)

    # Test with shorter thread info to ensure padding remains the same
    padded_thread_info_again = tracer.set_thread_info_padding(initial_thread_info)
    assert padded_thread_info_again == initial_thread_info.ljust(tracer.thread_info_padding)
    assert tracer.thread_info_padding == len(longer_thread_info)
