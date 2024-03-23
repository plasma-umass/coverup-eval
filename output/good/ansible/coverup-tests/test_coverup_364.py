# file lib/ansible/plugins/filter/mathstuff.py:128-137
# lines [128, 129, 130, 131, 133, 134, 136, 137]
# branches ['130->131', '130->133', '133->134', '133->136']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import min as min_filter
from jinja2.runtime import Context
from unittest.mock import MagicMock

# Mocking the HAS_MIN_MAX constant to simulate the environment where Jinja2 2.10 is not available
@pytest.fixture
def mock_has_min_max(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)

# Test function to cover the branch where HAS_MIN_MAX is False and kwargs are provided
def test_min_filter_with_kwargs_and_no_min_max(mock_has_min_max):
    environment = MagicMock(spec=Context)
    with pytest.raises(AnsibleFilterError) as excinfo:
        min_filter(environment, [1, 2, 3], unsupported_kwarg=True)
    assert "Ansible's min filter does not support any keyword arguments." in str(excinfo.value)

# Test function to cover the branch where HAS_MIN_MAX is False and no kwargs are provided
def test_min_filter_no_kwargs_and_no_min_max(mock_has_min_max):
    environment = MagicMock(spec=Context)
    result = min_filter(environment, [3, 1, 2])
    assert result == 1
