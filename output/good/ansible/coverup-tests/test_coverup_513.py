# file lib/ansible/plugins/filter/mathstuff.py:119-125
# lines [119, 120, 121, 122, 124, 125]
# branches ['121->122', '121->124']

import pytest
from ansible.plugins.filter.mathstuff import union
from jinja2.runtime import Context
from collections.abc import Hashable

# Mocking the unique function and the Environment
class MockEnvironment:
    def __init__(self):
        self.filters = {}

    def get_filters(self):
        return self.filters

@pytest.fixture
def mock_environment(mocker):
    env = MockEnvironment()
    mocker.patch('ansible.plugins.filter.mathstuff.unique', return_value='unique_called')
    return env

def test_union_with_hashable(mock_environment):
    # Hashable inputs
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])
    expected = frozenset([1, 2, 3, 4, 5])
    result = union(mock_environment, a, b)
    assert result == expected

def test_union_with_non_hashable(mock_environment):
    # Non-hashable inputs
    a = [1, 2, 3]
    b = [3, 4, 5]
    result = union(mock_environment, a, b)
    assert result == 'unique_called'

# Ensure that the test does not affect other tests by using a fixture
@pytest.fixture(autouse=True)
def clean_up():
    # Setup code if needed
    yield
    # Teardown code if needed
