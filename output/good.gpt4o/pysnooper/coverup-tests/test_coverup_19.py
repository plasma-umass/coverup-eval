# file pysnooper/variables.py:53-83
# lines [80, 83]
# branches []

import pytest
from pysnooper.variables import CommonVariable

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _format_key(self, key):
        return super()._format_key(key)
    
    def _get_value(self, main_value, key):
        return super()._get_value(main_value, key)

def test_format_key_not_implemented():
    var = TestCommonVariable('source', 'unambiguous_source', [])
    with pytest.raises(NotImplementedError):
        var._format_key('test_key')

def test_get_value_not_implemented():
    var = TestCommonVariable('source', 'unambiguous_source', [])
    with pytest.raises(NotImplementedError):
        var._get_value('main_value', 'test_key')
