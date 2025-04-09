# file pysnooper/variables.py:100-108
# lines [100, 101, 102, 104, 105, 107, 108]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the necessary imports from pysnooper
from pysnooper.variables import Keys
import pysnooper.utils as utils

@pytest.fixture
def mock_utils(mocker):
    mocker.patch('pysnooper.utils.get_shortish_repr', side_effect=lambda x: f"repr({x})")
    yield

def test_keys_class(mock_utils):
    source_code = "main_value"
    keys_instance = Keys(source_code)
    
    # Test _keys method
    main_value = {'a': 1, 'b': 2}
    assert keys_instance._keys(main_value) == main_value.keys()
    
    # Test _format_key method
    key = 'a'
    assert keys_instance._format_key(key) == '[repr(a)]'
    
    # Test _get_value method
    assert keys_instance._get_value(main_value, key) == 1
