# file: tornado/options.py:551-552
# asked: {"lines": [551, 552], "branches": []}
# gained: {"lines": [551, 552], "branches": []}

import pytest
from tornado.options import _Option

def test_option_value_with_default():
    option = _Option(name="test_option", default="default_value", type=str)
    assert option.value() == "default_value"

def test_option_value_with_set_value():
    option = _Option(name="test_option", default="default_value", type=str)
    option.set("new_value")
    assert option.value() == "new_value"
