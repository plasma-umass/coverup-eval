# file codetiming/_timer.py:22-32
# lines [22, 23, 24, 26, 27, 28, 29, 30, 31]
# branches []

import math
from codetiming import Timer
import pytest
from unittest.mock import Mock

# Test function to cover missing branches
def test_timer_context_manager_with_logger(mocker):
    # Mock the logger to ensure it's called without affecting other tests
    mock_logger = mocker.Mock()

    # Use the Timer as a context manager with a custom logger
    with Timer(logger=mock_logger):
        pass  # Simulate quick operation

    # Assert that the logger was called once
    mock_logger.assert_called_once()

    # Assert that the logger was called with a string containing the expected text
    args, _ = mock_logger.call_args
    assert isinstance(args[0], str)
    assert "Elapsed time:" in args[0]

# Test function to cover missing branches with a custom text callable
def test_timer_context_manager_with_text_callable(mocker):
    # Mock the logger to ensure it's called without affecting other tests
    mock_logger = mocker.Mock()

    # Define a custom text callable
    def custom_text(elapsed: float) -> str:
        return f"Custom text: {elapsed:.2f}"

    # Use the Timer with a custom text callable and a custom logger
    with Timer(text=custom_text, logger=mock_logger):
        pass  # Simulate quick operation

    # Assert that the logger was called once
    mock_logger.assert_called_once()

    # Assert that the logger was called with a string containing the expected custom text
    args, _ = mock_logger.call_args
    assert isinstance(args[0], str)
    assert "Custom text:" in args[0]

# Test function to cover missing branches with a name
def test_timer_context_manager_with_name(mocker):
    # Mock the logger to ensure it's called without affecting other tests
    mock_logger = mocker.Mock()

    # Use the Timer with a name and a custom logger
    with Timer(name="test_timer", logger=mock_logger):
        pass  # Simulate quick operation

    # Assert that the logger was called once
    mock_logger.assert_called_once()

    # Assert that the logger was called with a string containing the expected text
    args, _ = mock_logger.call_args
    assert isinstance(args[0], str)
    assert "Elapsed time:" in args[0]
    # The name is not included in the default text, so we should not assert its presence
