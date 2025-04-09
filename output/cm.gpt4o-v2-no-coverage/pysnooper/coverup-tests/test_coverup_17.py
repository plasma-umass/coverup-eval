# file: pysnooper/variables.py:100-108
# asked: {"lines": [100, 101, 102, 104, 105, 107, 108], "branches": []}
# gained: {"lines": [100, 101, 102, 104, 105, 107, 108], "branches": []}

import pytest
from pysnooper.variables import Keys
from pysnooper import utils

class TestKeys:
    
    @pytest.fixture
    def keys_instance(self, mocker):
        mock_source = "mock_source"
        return Keys(mock_source)
    
    def test_keys_method(self, keys_instance):
        test_dict = {'a': 1, 'b': 2}
        result = keys_instance._keys(test_dict)
        assert result == test_dict.keys()
    
    def test_format_key_method(self, keys_instance, mocker):
        key = 'test_key'
        mocker.patch('pysnooper.utils.get_shortish_repr', return_value='short_repr')
        result = keys_instance._format_key(key)
        assert result == '[short_repr]'
        utils.get_shortish_repr.assert_called_once_with(key)
    
    def test_get_value_method(self, keys_instance):
        test_dict = {'a': 1, 'b': 2}
        result = keys_instance._get_value(test_dict, 'a')
        assert result == 1
        result = keys_instance._get_value(test_dict, 'b')
        assert result == 2
