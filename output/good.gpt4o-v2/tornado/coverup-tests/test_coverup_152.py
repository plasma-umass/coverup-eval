# file: tornado/options.py:462-464
# asked: {"lines": [462, 464], "branches": []}
# gained: {"lines": [462, 464], "branches": []}

import pytest
from tornado.options import OptionParser

def test_add_parse_callback():
    parser = OptionParser()
    callback_called = False

    def sample_callback():
        nonlocal callback_called
        callback_called = True

    parser.add_parse_callback(sample_callback)
    assert sample_callback in parser._parse_callbacks

    # Simulate the end of option parsing to trigger the callback
    parser.run_parse_callbacks()
    assert callback_called
