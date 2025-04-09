# file lib/ansible/plugins/filter/mathstuff.py:109-116
# lines [109, 110, 111, 112, 114, 115, 116]
# branches ['111->112', '111->114']

import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference
from jinja2.runtime import Context
from collections.abc import Hashable

# Mocking the intersect and union functions as they are not provided in the snippet
def mock_intersect(environment, a, b):
    return [x for x in a if x in b]

def mock_union(environment, a, b):
    return list(set(a).union(b))

@pytest.fixture
def mock_environment(mocker):
    environment = mocker.MagicMock(spec=Context)
    mocker.patch('ansible.plugins.filter.mathstuff.intersect', side_effect=mock_intersect)
    mocker.patch('ansible.plugins.filter.mathstuff.union', side_effect=mock_union)
    return environment

def test_symmetric_difference_with_hashable(mock_environment):
    # Hashable inputs
    a = {1, 2, 3}
    b = {3, 4, 5}
    expected = {1, 2, 4, 5}
    result = symmetric_difference(mock_environment, a, b)
    assert set(result) == expected, "The symmetric difference of hashable sets is incorrect"

def test_symmetric_difference_with_non_hashable(mock_environment):
    # Non-hashable inputs
    a = [1, 2, 2, 3]
    b = [3, 3, 4, 5]
    expected = [1, 2, 4, 5]
    result = symmetric_difference(mock_environment, a, b)
    assert sorted(result) == sorted(expected), "The symmetric difference of non-hashable lists is incorrect"

# Run the tests
if __name__ == "__main__":
    pytest.main()
