# file pysnooper/tracer.py:41-43
# lines [41, 42, 43]
# branches []

import pytest
from pysnooper.tracer import UnavailableSource

def test_unavailable_source():
    source = UnavailableSource()
    assert source[0] == u'SOURCE IS UNAVAILABLE'
    assert source[1] == u'SOURCE IS UNAVAILABLE'
    assert source[-1] == u'SOURCE IS UNAVAILABLE'
