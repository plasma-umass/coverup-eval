# file: pysnooper/tracer.py:41-43
# asked: {"lines": [41, 42, 43], "branches": []}
# gained: {"lines": [41, 42, 43], "branches": []}

import pytest

def test_unavailable_source_getitem():
    from pysnooper.tracer import UnavailableSource

    source = UnavailableSource()
    assert source[0] == 'SOURCE IS UNAVAILABLE'
    assert source[1] == 'SOURCE IS UNAVAILABLE'
    assert source[-1] == 'SOURCE IS UNAVAILABLE'
