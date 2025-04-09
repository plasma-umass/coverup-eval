# file tornado/options.py:470-485
# lines [485]
# branches []

import pytest
from unittest.mock import patch
from tornado.options import OptionParser

class _Mockable:
    def __init__(self, obj):
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        setattr(self._obj, name, value)

# Add the _Mockable class to the tornado.options module for testing purposes
setattr(OptionParser, "_Mockable", _Mockable)

@pytest.fixture
def option_parser():
    parser = OptionParser()
    parser.define("test_option", default=None)
    return parser

def test_mockable(option_parser):
    with patch.object(option_parser.mockable(), 'test_option', 'test_value'):
        assert option_parser.test_option == 'test_value'
