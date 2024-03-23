# file tornado/escape.py:91-103
# lines [91, 102, 103]
# branches []

import pytest
from tornado.escape import url_escape

def test_url_escape():
    # Test with plus=True, which should use quote_plus
    assert url_escape("test value") == "test+value"
    assert url_escape(" ") == "+"

    # Test with plus=False, which should use quote
    assert url_escape("test value", plus=False) == "test%20value"
    assert url_escape(" ", plus=False) == "%20"

    # Test with bytes input
    assert url_escape(b"test value") == "test+value"
    assert url_escape(b" ", plus=False) == "%20"

    # Clean up is not necessary as url_escape does not modify any global state
