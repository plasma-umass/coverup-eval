# file: lib/ansible/module_utils/api.py:138-166
# asked: {"lines": [145, 153, 155, 156, 157, 158, 159, 160, 161, 164], "branches": [[144, 145], [155, 156], [155, 164], [159, 160], [159, 161]]}
# gained: {"lines": [145, 153, 155, 156, 157, 158, 159, 160, 161, 164], "branches": [[144, 145], [155, 156], [155, 164], [159, 160], [159, 161]]}

import pytest
import time
from unittest.mock import Mock, patch

# Assuming the retry_with_delays_and_condition and retry_never are defined in ansible/module_utils/api.py
from ansible.module_utils.api import retry_with_delays_and_condition, retry_never

def test_retry_with_delays_and_condition_no_retry(monkeypatch):
    mock_function = Mock(side_effect=ValueError("Test exception"))
    backoff_iterator = iter([1, 2, 3])

    @retry_with_delays_and_condition(backoff_iterator)
    def wrapped_function():
        return mock_function()

    with pytest.raises(ValueError, match="Test exception"):
        wrapped_function()

    assert mock_function.call_count == 1

def test_retry_with_delays_and_condition_with_retry(monkeypatch):
    mock_function = Mock(side_effect=[ValueError("Test exception"), "Success"])
    backoff_iterator = iter([1, 2, 3])

    def should_retry_error(exception):
        return isinstance(exception, ValueError)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def wrapped_function():
        return mock_function()

    result = wrapped_function()
    assert result == "Success"
    assert mock_function.call_count == 2

def test_retry_with_delays_and_condition_exhaust_retries(monkeypatch):
    mock_function = Mock(side_effect=ValueError("Test exception"))
    backoff_iterator = iter([1, 2, 3])

    def should_retry_error(exception):
        return isinstance(exception, ValueError)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def wrapped_function():
        return mock_function()

    with pytest.raises(ValueError, match="Test exception"):
        wrapped_function()

    assert mock_function.call_count == 4

def test_retry_with_delays_and_condition_no_delays(monkeypatch):
    mock_function = Mock(return_value="Success")
    backoff_iterator = iter([])

    @retry_with_delays_and_condition(backoff_iterator)
    def wrapped_function():
        return mock_function()

    result = wrapped_function()
    assert result == "Success"
    assert mock_function.call_count == 1
