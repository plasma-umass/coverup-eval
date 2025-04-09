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

def test_retry_with_delays_and_condition_no_retry(monkeypatch):
    # Mock function to be decorated
    mock_function = Mock(side_effect=ValueError("Test error"))
    
    # Mock time.sleep to avoid actual delays
    monkeypatch.setattr(time, 'sleep', Mock())
    
    # Create a backoff iterator with some delays
    backoff_iterator = iter([1, 2, 3])
    
    # Decorate the mock function
    decorated_function = retry_with_delays_and_condition(backoff_iterator)(mock_function)
    
    # Call the decorated function and expect it to raise the exception
    with pytest.raises(ValueError, match="Test error"):
        decorated_function()
    
    # Ensure the function was called only once (no retries)
    assert mock_function.call_count == 1

def test_retry_with_delays_and_condition_with_retry(monkeypatch):
    # Mock function to be decorated
    mock_function = Mock(side_effect=[ValueError("Test error"), "Success"])
    
    # Mock time.sleep to avoid actual delays
    monkeypatch.setattr(time, 'sleep', Mock())
    
    # Create a backoff iterator with some delays
    backoff_iterator = iter([1, 2, 3])
    
    # Define a should_retry_error function that retries on ValueError
    def should_retry_error(exception):
        return isinstance(exception, ValueError)
    
    # Decorate the mock function
    decorated_function = retry_with_delays_and_condition(backoff_iterator, should_retry_error)(mock_function)
    
    # Call the decorated function and expect it to return "Success"
    result = decorated_function()
    
    # Ensure the function was called twice (one retry)
    assert mock_function.call_count == 2
    assert result == "Success"

def test_retry_with_delays_and_condition_exhaust_retries(monkeypatch):
    # Mock function to be decorated
    mock_function = Mock(side_effect=ValueError("Test error"))
    
    # Mock time.sleep to avoid actual delays
    monkeypatch.setattr(time, 'sleep', Mock())
    
    # Create a backoff iterator with some delays
    backoff_iterator = iter([1, 2, 3])
    
    # Define a should_retry_error function that retries on ValueError
    def should_retry_error(exception):
        return isinstance(exception, ValueError)
    
    # Decorate the mock function
    decorated_function = retry_with_delays_and_condition(backoff_iterator, should_retry_error)(mock_function)
    
    # Call the decorated function and expect it to raise the exception after exhausting retries
    with pytest.raises(ValueError, match="Test error"):
        decorated_function()
    
    # Ensure the function was called four times (three retries + one final attempt)
    assert mock_function.call_count == 4
