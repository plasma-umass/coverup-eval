# file: lib/ansible/module_utils/api.py:138-166
# asked: {"lines": [145, 153, 155, 156, 157, 158, 159, 160, 161, 164], "branches": [[144, 145], [155, 156], [155, 164], [159, 160], [159, 161]]}
# gained: {"lines": [145, 153, 155, 156, 157, 158, 159, 160, 161, 164], "branches": [[144, 145], [155, 156], [155, 164], [159, 160], [159, 161]]}

import pytest
import time
from unittest.mock import Mock

# Assuming the retry_with_delays_and_condition and retry_never functions are defined in ansible.module_utils.api
from ansible.module_utils.api import retry_with_delays_and_condition, retry_never

def test_retry_with_delays_and_condition_no_retries(monkeypatch):
    mock_function = Mock(side_effect=[ValueError("Test error"), "Success"])
    backoff_iterator = [1, 2, 3]

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error=retry_never)
    def wrapped_function():
        return mock_function()

    with pytest.raises(ValueError, match="Test error"):
        wrapped_function()
    
    assert mock_function.call_count == 1

def test_retry_with_delays_and_condition_with_retries(monkeypatch):
    mock_function = Mock(side_effect=[ValueError("Test error"), "Success"])
    backoff_iterator = [1, 2, 3]

    def should_retry_error(exception):
        return isinstance(exception, ValueError)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error=should_retry_error)
    def wrapped_function():
        return mock_function()

    monkeypatch.setattr(time, 'sleep', lambda x: None)  # To avoid actual delay

    result = wrapped_function()
    
    assert result == "Success"
    assert mock_function.call_count == 2

def test_retry_with_delays_and_condition_no_delays(monkeypatch):
    mock_function = Mock(return_value="Success")
    backoff_iterator = []

    @retry_with_delays_and_condition(backoff_iterator)
    def wrapped_function():
        return mock_function()

    result = wrapped_function()
    
    assert result == "Success"
    assert mock_function.call_count == 1
