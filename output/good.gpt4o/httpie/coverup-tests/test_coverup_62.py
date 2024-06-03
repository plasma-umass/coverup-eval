# file httpie/utils.py:18-19
# lines [18, 19]
# branches []

import pytest
from httpie.utils import repr_dict
from unittest.mock import patch
from pprint import pformat

def test_repr_dict():
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    
    # Mocking pformat to ensure it is called correctly
    with patch('httpie.utils.pformat', wraps=pformat) as mock_pformat:
        result = repr_dict(test_dict)
        
        # Ensure pformat was called with the correct argument
        mock_pformat.assert_called_once_with(test_dict)
        
        # Ensure the result is as expected
        expected_result = pformat(test_dict)
        assert result == expected_result
