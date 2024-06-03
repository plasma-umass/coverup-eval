# file pysnooper/utils.py:67-78
# lines [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]
# branches ['74->75', '74->76', '76->77', '76->78']

import pytest
from unittest.mock import Mock, patch
from pysnooper.utils import get_shortish_repr, truncate

def test_get_shortish_repr():
    # Mocking get_repr_function to control the repr function
    mock_repr_function = Mock()
    mock_repr_function.side_effect = lambda x: repr(x)
    
    # Patching get_repr_function to return our mock
    with patch('pysnooper.utils.get_repr_function', return_value=mock_repr_function):
        # Test with a normal object
        item = "test"
        result = get_shortish_repr(item)
        assert result == repr(item).replace('\r', '').replace('\n', '')

        # Test with an object that raises an exception in repr
        class BadRepr:
            def __repr__(self):
                raise ValueError("bad repr")
        
        bad_item = BadRepr()
        result = get_shortish_repr(bad_item)
        assert result == 'REPR FAILED'

        # Test with normalize=True
        item = "test\n"
        result = get_shortish_repr(item, normalize=True)
        assert result == repr(item).replace('\r', '').replace('\n', '')

        # Test with max_length
        item = "test"
        result = get_shortish_repr(item, max_length=2)
        assert result == truncate(repr(item).replace('\r', '').replace('\n', ''), 2)

        # Test with both normalize and max_length
        item = "test\n"
        result = get_shortish_repr(item, normalize=True, max_length=2)
        assert result == truncate(repr(item).replace('\r', '').replace('\n', ''), 2)
