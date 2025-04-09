# file: lib/ansible/plugins/filter/mathstuff.py:100-106
# asked: {"lines": [102, 103, 105, 106], "branches": [[102, 103], [102, 105]]}
# gained: {"lines": [102, 103, 105, 106], "branches": [[102, 103], [102, 105]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.filter.mathstuff import difference
from ansible.module_utils.common._collections_compat import Hashable

@pytest.fixture
def mock_environment():
    return MagicMock()

def test_difference_hashable(mock_environment):
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = difference(mock_environment, a, b)
    assert result == {1}

def test_difference_non_hashable(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.unique', return_value=[1, 2]) as mock_unique:
        a = [1, 2, 3, 4]
        b = [3, 4, 5, 6]
        result = difference(mock_environment, a, b)
        mock_unique.assert_called_once_with(mock_environment, [1, 2], True)
        assert result == [1, 2]
