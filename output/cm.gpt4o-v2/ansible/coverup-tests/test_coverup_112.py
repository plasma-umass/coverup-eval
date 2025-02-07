# file: lib/ansible/module_utils/api.py:138-166
# asked: {"lines": [138, 144, 145, 147, 148, 149, 153, 155, 156, 157, 158, 159, 160, 161, 164, 165, 166], "branches": [[144, 145], [144, 147], [155, 156], [155, 164], [159, 160], [159, 161]]}
# gained: {"lines": [138, 144, 145, 147, 148, 149, 153, 155, 156, 157, 158, 159, 160, 161, 164, 165, 166], "branches": [[144, 145], [144, 147], [155, 156], [155, 164], [159, 160], [159, 161]]}

import pytest
import time
from unittest.mock import Mock

from ansible.module_utils.api import retry_with_delays_and_condition

def test_retry_with_delays_and_condition_no_retries(monkeypatch):
    mock_function = Mock(side_effect=ValueError("Test error"))
    backoff_iterator = iter([0.1, 0.2, 0.3])

    @retry_with_delays_and_condition(backoff_iterator)
    def test_func():
        return mock_function()

    with pytest.raises(ValueError, match="Test error"):
        test_func()

    assert mock_function.call_count == 1

def test_retry_with_delays_and_condition_with_retries(monkeypatch):
    mock_function = Mock(side_effect=[ValueError("Test error"), ValueError("Test error"), "Success"])
    backoff_iterator = iter([0.1, 0.2, 0.3])

    def should_retry_error(exception):
        return isinstance(exception, ValueError)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def test_func():
        return mock_function()

    result = test_func()
    assert result == "Success"
    assert mock_function.call_count == 3

def test_retry_with_delays_and_condition_final_attempt(monkeypatch):
    mock_function = Mock(side_effect=[ValueError("Test error"), "Success"])
    backoff_iterator = iter([0.1])

    def should_retry_error(exception):
        return isinstance(exception, ValueError)

    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def test_func():
        return mock_function()

    result = test_func()
    assert result == "Success"
    assert mock_function.call_count == 2
