# file: pysnooper/variables.py:100-108
# asked: {"lines": [100, 101, 102, 104, 105, 107, 108], "branches": []}
# gained: {"lines": [100, 101, 102, 104, 105, 107, 108], "branches": []}

import pytest
from pysnooper.variables import Keys
from pysnooper import utils

class TestKeys:
    
    @pytest.fixture
    def keys_instance(self):
        source = 'dummy_source'
        return Keys(source)
    
    def test_keys_method(self, keys_instance):
        main_value = {'a': 1, 'b': 2}
        result = keys_instance._keys(main_value)
        assert result == main_value.keys()
    
    def test_format_key_method(self, keys_instance, mocker):
        key = 'test_key'
        mocker.patch('pysnooper.utils.get_shortish_repr', return_value='short_repr')
        result = keys_instance._format_key(key)
        assert result == '[short_repr]'
    
    def test_get_value_method(self, keys_instance):
        main_value = {'a': 1, 'b': 2}
        key = 'a'
        result = keys_instance._get_value(main_value, key)
        assert result == 1
