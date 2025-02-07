# file: tornado/options.py:660-661
# asked: {"lines": [660, 661], "branches": []}
# gained: {"lines": [660, 661], "branches": []}

import pytest
from tornado.options import _Option

@pytest.fixture
def option():
    return _Option(name="test_option", default=None, type=str)

def test_parse_bool_true(option):
    assert option._parse_bool("true") == True
    assert option._parse_bool("1") == True
    assert option._parse_bool("t") == True
    assert option._parse_bool("yes") == True

def test_parse_bool_false(option):
    assert option._parse_bool("false") == False
    assert option._parse_bool("0") == False
    assert option._parse_bool("f") == False
    assert option._parse_bool("no") == True  # This is to check that "no" is not considered false
