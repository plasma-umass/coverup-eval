# file semantic_release/ci_checks.py:9-27
# lines [9, 18, 19, 20, 21, 22, 23, 24, 27]
# branches []

import pytest
from semantic_release.ci_checks import CiVerificationError, checker

def test_checker_raises_ci_verification_error(mocker):
    # Mock a function that will raise an AssertionError
    mock_func = mocker.Mock(side_effect=AssertionError("assertion error"))

    # Apply the checker decorator to the mock function
    @checker
    def wrapped_func():
        mock_func()

    # Assert that the CiVerificationError is raised when the wrapped function is called
    with pytest.raises(CiVerificationError) as exc_info:
        wrapped_func()

    # Verify the exception message
    assert str(exc_info.value) == "The verification check for the environment did not pass."

    # Verify that the mock function was indeed called
    mock_func.assert_called_once()

def test_checker_returns_true_on_success(mocker):
    # Mock a function that does not raise an exception
    mock_func = mocker.Mock()

    # Apply the checker decorator to the mock function
    @checker
    def wrapped_func():
        mock_func()

    # Call the wrapped function and assert that it returns True
    assert wrapped_func() is True

    # Verify that the mock function was indeed called
    mock_func.assert_called_once()
