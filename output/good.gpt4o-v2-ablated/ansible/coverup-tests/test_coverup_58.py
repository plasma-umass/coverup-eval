# file: lib/ansible/module_utils/api.py:138-166
# asked: {"lines": [138, 144, 145, 147, 148, 149, 153, 155, 156, 157, 158, 159, 160, 161, 164, 165, 166], "branches": [[144, 145], [144, 147], [155, 156], [155, 164], [159, 160], [159, 161]]}
# gained: {"lines": [138, 144, 145, 147, 148, 149, 153, 155, 156, 157, 158, 159, 160, 161, 164, 165, 166], "branches": [[144, 145], [144, 147], [155, 156], [155, 164], [159, 160], [159, 161]]}

import pytest
import time
import functools
from unittest.mock import Mock, patch

# Assuming retry_never is defined somewhere in the module
def retry_never(exception):
    return False

# Import the function to be tested
from ansible.module_utils.api import retry_with_delays_and_condition

def test_retry_with_no_delays():
    mock_function = Mock(return_value="success")
    decorated_function = retry_with_delays_and_condition([])(mock_function)
    
    result = decorated_function()
    
    mock_function.assert_called_once()
    assert result == "success"

def test_retry_with_delays_and_no_retry():
    mock_function = Mock(side_effect=[Exception("fail"), "success"])
    decorated_function = retry_with_delays_and_condition([0.1])(mock_function)
    
    with pytest.raises(Exception, match="fail"):
        decorated_function()
    
    assert mock_function.call_count == 1

def test_retry_with_delays_and_retry():
    mock_function = Mock(side_effect=[Exception("fail"), "success"])
    should_retry_error = Mock(side_effect=lambda e: isinstance(e, Exception))
    decorated_function = retry_with_delays_and_condition([0.1], should_retry_error)(mock_function)
    
    with patch('time.sleep', return_value=None):
        result = decorated_function()
    
    assert mock_function.call_count == 2
    assert result == "success"

def test_retry_with_multiple_delays_and_retry():
    mock_function = Mock(side_effect=[Exception("fail"), Exception("fail again"), "success"])
    should_retry_error = Mock(side_effect=lambda e: isinstance(e, Exception))
    decorated_function = retry_with_delays_and_condition([0.1, 0.2], should_retry_error)(mock_function)
    
    with patch('time.sleep', return_value=None):
        result = decorated_function()
    
    assert mock_function.call_count == 3
    assert result == "success"

def test_retry_with_final_attempt():
    mock_function = Mock(side_effect=[Exception("fail"), Exception("fail again"), "success"])
    should_retry_error = Mock(side_effect=lambda e: isinstance(e, Exception))
    decorated_function = retry_with_delays_and_condition([0.1, 0.2], should_retry_error)(mock_function)
    
    with patch('time.sleep', return_value=None):
        result = decorated_function()
    
    assert mock_function.call_count == 3
    assert result == "success"

def test_retry_with_no_retry_condition():
    mock_function = Mock(side_effect=[Exception("fail"), "success"])
    decorated_function = retry_with_delays_and_condition([0.1])(mock_function)
    
    with pytest.raises(Exception, match="fail"):
        decorated_function()
    
    assert mock_function.call_count == 1
