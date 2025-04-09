# file: tornado/options.py:488-515
# asked: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}
# gained: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}

import pytest
from tornado.options import OptionParser

# Assuming the _Mockable class is accessible from the module
from tornado.options import _Mockable

@pytest.fixture
def option_parser():
    return OptionParser()

@pytest.fixture
def mockable(option_parser):
    return _Mockable(option_parser)

def test_mockable_getattr(mockable, option_parser):
    option_parser.define("test_option", default="default_value")
    assert mockable.test_option == "default_value"

def test_mockable_setattr(mockable, option_parser):
    option_parser.define("test_option", default="default_value")
    mockable.test_option = "new_value"
    assert mockable.test_option == "new_value"
    assert option_parser.test_option == "new_value"

def test_mockable_setattr_reuse(mockable, option_parser):
    option_parser.define("test_option", default="default_value")
    mockable.test_option = "new_value"
    with pytest.raises(AssertionError, match="don't reuse mockable objects"):
        mockable.test_option = "another_value"

def test_mockable_delattr(mockable, option_parser):
    option_parser.define("test_option", default="default_value")
    mockable.test_option = "new_value"
    del mockable.test_option
    assert mockable.test_option == "default_value"
    assert option_parser.test_option == "default_value"
