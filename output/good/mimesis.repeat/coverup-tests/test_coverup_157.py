# file mimesis/providers/internet.py:69-77
# lines [69, 77]
# branches []

import pytest
from mimesis.providers.internet import Internet

# Mock the random.choice method to ensure that all branches are covered
@pytest.fixture
def mock_random_choice(mocker):
    return mocker.patch('mimesis.random.Random.choice')

# Test function to cover the http_status_code method
def test_http_status_code(mock_random_choice):
    internet = Internet()

    # Mock the return value to be a specific HTTP status code
    mock_random_choice.return_value = 404

    # Call the method under test
    status_code = internet.http_status_code()

    # Assert that the mocked method was called once
    mock_random_choice.assert_called_once()

    # Assert that the returned status code is the one we mocked
    assert status_code == 404

    # Clean up by stopping the mock
    mock_random_choice.stop()
