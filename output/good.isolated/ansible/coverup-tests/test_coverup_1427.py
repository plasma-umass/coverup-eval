# file lib/ansible/plugins/filter/mathstuff.py:109-116
# lines [112]
# branches ['111->112']

import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference
from jinja2.runtime import Context
from collections.abc import Hashable

# Mocking the environment to pass to the filter function
@pytest.fixture
def mock_environment(mocker):
    return mocker.MagicMock(spec=Context)

# Test function to cover line 112
def test_symmetric_difference_with_hashable(mock_environment):
    # Create two hashable objects
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])

    # Ensure both objects are instances of Hashable
    assert isinstance(a, Hashable)
    assert isinstance(b, Hashable)

    # Call the symmetric_difference function
    result = symmetric_difference(mock_environment, a, b)

    # Verify the result is the symmetric difference of the two sets
    expected_result = frozenset([1, 2, 4, 5])
    assert result == expected_result, "The result should be the symmetric difference of two sets"
