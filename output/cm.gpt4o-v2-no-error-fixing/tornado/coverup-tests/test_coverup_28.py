# file: tornado/options.py:488-515
# asked: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}
# gained: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}

import pytest
from unittest import mock
from tornado.options import OptionParser

# Assuming _Mockable is defined in tornado.options
from tornado.options import _Mockable

@pytest.fixture
def option_parser():
    return OptionParser()

@pytest.fixture
def mockable(option_parser):
    return _Mockable(option_parser)

def test_mockable_getattr(mockable, option_parser):
    option_parser.define("test_option", default=42)
    assert mockable.test_option == 42

def test_mockable_setattr(mockable, option_parser):
    option_parser.define("test_option", default=42)
    mockable.test_option = 100
    assert mockable.test_option == 100
    assert option_parser.test_option == 100

def test_mockable_setattr_reuse(mockable, option_parser):
    option_parser.define("test_option", default=42)
    mockable.test_option = 100
    with pytest.raises(AssertionError, match="don't reuse mockable objects"):
        mockable.test_option = 200

def test_mockable_delattr(mockable, option_parser):
    option_parser.define("test_option", default=42)
    mockable.test_option = 100
    del mockable.test_option
    assert option_parser.test_option == 42
