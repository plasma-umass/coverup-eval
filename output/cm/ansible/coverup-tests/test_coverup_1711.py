# file lib/ansible/plugins/filter/mathstuff.py:140-149
# lines [143]
# branches ['142->143']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.filter.mathstuff import max as max_filter

# Mocking the HAS_MIN_MAX constant to force the execution of the if branch
@pytest.fixture
def mock_has_min_max(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)

# Mocking the do_max function to check if it's being called
@pytest.fixture
def mock_do_max(mocker):
    return mocker.patch('ansible.plugins.filter.mathstuff.do_max', return_value='mocked_max')

def test_max_filter_with_has_min_max(mock_has_min_max, mock_do_max):
    environment = MagicMock()
    result = max_filter(environment, [1, 2, 3], some_kwarg=True)
    mock_do_max.assert_called_once_with(environment, [1, 2, 3], some_kwarg=True)
    assert result == 'mocked_max'
