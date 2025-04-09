# file pysnooper/variables.py:53-83
# lines [80, 83]
# branches []

import pytest
from pysnooper.variables import CommonVariable

class TestCommonVariable(CommonVariable):
    def _keys(self, main_value):
        return ['key1']

def test_common_variable_format_key_and_get_value():
    common_variable = TestCommonVariable('source', exclude=[])

    with pytest.raises(NotImplementedError):
        common_variable._format_key('key')

    with pytest.raises(NotImplementedError):
        common_variable._get_value('main_value', 'key')
