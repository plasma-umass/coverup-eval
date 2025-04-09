# file: pysnooper/variables.py:53-83
# asked: {"lines": [77, 80, 83], "branches": []}
# gained: {"lines": [77, 80, 83], "branches": []}

import pytest
from pysnooper.variables import CommonVariable
from pysnooper import utils

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _keys(self, main_value):
        return super()._keys(main_value)

    def _format_key(self, key):
        return super()._format_key(key)

    def _get_value(self, main_value, key):
        return super()._get_value(main_value, key)

def test_keys():
    var = TestCommonVariable('source', 'unambiguous_source', [])
    assert var._keys('any_value') == ()

def test_format_key():
    var = TestCommonVariable('source', 'unambiguous_source', [])
    with pytest.raises(NotImplementedError):
        var._format_key('any_key')

def test_get_value():
    var = TestCommonVariable('source', 'unambiguous_source', [])
    with pytest.raises(NotImplementedError):
        var._get_value('main_value', 'any_key')
