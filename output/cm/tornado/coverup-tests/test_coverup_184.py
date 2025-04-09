# file tornado/options.py:660-661
# lines [660, 661]
# branches []

import pytest
from tornado.options import _Option

@pytest.fixture
def option_instance():
    return _Option(name='test_option', type=str)

def test_parse_bool_true(option_instance):
    assert option_instance._parse_bool("true")
    assert option_instance._parse_bool("1")
    assert option_instance._parse_bool("T")
    assert option_instance._parse_bool("yes")
    assert option_instance._parse_bool("y")

def test_parse_bool_false(option_instance):
    assert not option_instance._parse_bool("false")
    assert not option_instance._parse_bool("0")
    assert not option_instance._parse_bool("f")

def test_parse_bool_case_insensitive(option_instance):
    assert option_instance._parse_bool("TrUe")
    assert not option_instance._parse_bool("FaLsE")
