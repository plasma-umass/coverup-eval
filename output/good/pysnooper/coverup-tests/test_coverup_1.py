# file pysnooper/tracer.py:41-43
# lines [41, 42, 43]
# branches []

import pytest
from pysnooper.tracer import UnavailableSource

def test_unavailable_source_getitem():
    unavailable_source = UnavailableSource()
    assert unavailable_source[0] == u'SOURCE IS UNAVAILABLE'
    assert unavailable_source[1] == u'SOURCE IS UNAVAILABLE'
    assert unavailable_source[100] == u'SOURCE IS UNAVAILABLE'
    assert unavailable_source[-1] == u'SOURCE IS UNAVAILABLE'
