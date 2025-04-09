# file: tornado/options.py:462-464
# asked: {"lines": [462, 464], "branches": []}
# gained: {"lines": [462, 464], "branches": []}

import pytest
from tornado.options import OptionParser

def test_add_parse_callback():
    parser = OptionParser()
    callback_called = False

    def callback():
        nonlocal callback_called
        callback_called = True

    parser.add_parse_callback(callback)
    assert callback in parser._parse_callbacks

    # Simulate running the parse callbacks
    for cb in parser._parse_callbacks:
        cb()

    assert callback_called
