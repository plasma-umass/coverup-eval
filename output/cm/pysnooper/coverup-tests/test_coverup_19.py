# file pysnooper/variables.py:100-108
# lines [100, 101, 102, 104, 105, 107, 108]
# branches []

import pytest
from pysnooper.variables import Keys
from pysnooper import utils

class TestKeys:
    @pytest.fixture
    def keys_instance(self):
        return Keys(source='dict_var', exclude=())

    def test_keys(self, keys_instance):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        assert list(keys_instance._keys(test_dict)) == ['a', 'b', 'c']

    def test_format_key(self, keys_instance):
        key = 'test_key'
        formatted_key = keys_instance._format_key(key)
        assert formatted_key == '[{}]'.format(utils.get_shortish_repr(key))

    def test_get_value(self, keys_instance):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        for key, value in test_dict.items():
            assert keys_instance._get_value(test_dict, key) == value
