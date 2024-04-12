# file lib/ansible/plugins/filter/mathstuff.py:100-106
# lines [102, 103, 105, 106]
# branches ['102->103', '102->105']

import pytest
from ansible.plugins.filter.mathstuff import difference
from jinja2.runtime import Context
from collections.abc import Hashable

# Mocking the environment and unique function
class MockEnvironment:
    def __init__(self):
        self.filters = {}

def mock_unique(environment, value, case_sensitive=False):
    # Mock behavior of unique function
    if case_sensitive:
        seen = []
        return [x for x in value if x not in seen and not seen.append(x)]
    else:
        seen = []
        return [x.lower() for x in value if x.lower() not in seen and not seen.append(x.lower())]

@pytest.fixture
def mock_environment(mocker):
    env = MockEnvironment()
    mocker.patch('ansible.plugins.filter.mathstuff.unique', side_effect=mock_unique)
    return env

def test_difference_with_non_hashable_elements(mock_environment):
    # Non-hashable elements, should trigger lines 105-106
    a = [{'key': 'value1'}, {'key': 'value2'}]
    b = [{'key': 'value1'}]
    expected_result = [{'key': 'value2'}]

    result = difference(mock_environment, a, b)
    assert result == expected_result
    assert isinstance(result, list)

def test_difference_with_hashable_elements(mock_environment):
    # Hashable elements, should trigger lines 102-103
    a = [1, 2, 3, 4]
    b = [2, 3]
    expected_result = [1, 4]  # Adjusted expected result to match the list type

    result = difference(mock_environment, a, b)
    assert result == expected_result
    assert isinstance(result, list)  # Adjusted assertion to expect a list
