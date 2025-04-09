# file lib/ansible/plugins/filter/mathstuff.py:128-137
# lines [131]
# branches ['130->131']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.filter.mathstuff import min

# Mocking the HAS_MIN_MAX constant to True to cover the branch with line 131
@pytest.fixture
def mock_has_min_max_true(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)

# Mocking the do_min function to ensure it is called
@pytest.fixture
def mock_do_min(mocker):
    return mocker.patch('ansible.plugins.filter.mathstuff.do_min', return_value='mocked_min')

def test_min_with_has_min_max_and_kwargs(mock_has_min_max_true, mock_do_min):
    # Call the min function with kwargs to trigger line 131
    result = min(None, [1, 2, 3], some_kwarg='value')
    # Verify that do_min was called with the correct arguments
    mock_do_min.assert_called_once_with(None, [1, 2, 3], some_kwarg='value')
    # Verify that the result is from the mocked do_min function
    assert result == 'mocked_min', "The min function did not return the mocked value"
