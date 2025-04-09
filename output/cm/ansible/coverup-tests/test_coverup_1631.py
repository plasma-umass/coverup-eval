# file lib/ansible/plugins/filter/mathstuff.py:91-97
# lines [93, 94, 96, 97]
# branches ['93->94', '93->96']

import pytest
from ansible.plugins.filter.mathstuff import intersect
from jinja2.runtime import Context
from collections.abc import Hashable

# Mocking the environment and unique function
class MockEnvironment:
    def __init__(self):
        self.filters = {}

@pytest.fixture
def mock_environment(mocker):
    env = MockEnvironment()
    mocker.patch('ansible.plugins.filter.mathstuff.unique', return_value='unique_called')
    return env

def test_intersect_non_hashable_elements(mock_environment):
    # Non-hashable elements should take the else branch (lines 96-97)
    a = [1, 2, [3]]  # [3] is not hashable
    b = [2, [3], 4]
    result = intersect(mock_environment, a, b)
    assert result == 'unique_called', "The result should be the output of the unique function"

def test_intersect_hashable_elements(mock_environment):
    # Hashable elements should take the if branch (lines 93-94)
    a = (1, 2, 3)
    b = (2, 3, 4)
    result = intersect(mock_environment, a, b)
    assert result == {2, 3}, "The result should be the intersection of sets a and b"
