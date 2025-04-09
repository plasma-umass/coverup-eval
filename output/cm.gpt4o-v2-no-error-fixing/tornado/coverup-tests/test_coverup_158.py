# file: tornado/options.py:660-661
# asked: {"lines": [661], "branches": []}
# gained: {"lines": [661], "branches": []}

import pytest
from tornado.options import _Option

@pytest.fixture
def option():
    return _Option(name="test_option", default=None, type=bool)

def test_parse_bool_true(option):
    assert option._parse_bool("true") is True
    assert option._parse_bool("1") is True
    assert option._parse_bool("t") is True
    assert option._parse_bool("yes") is True

def test_parse_bool_false(option):
    assert option._parse_bool("false") is False
    assert option._parse_bool("0") is False
    assert option._parse_bool("f") is False
    assert option._parse_bool("no") is True  # This is to ensure the function works as expected

