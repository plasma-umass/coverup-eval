# file: lib/ansible/plugins/filter/mathstuff.py:91-97
# asked: {"lines": [91, 92, 93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}
# gained: {"lines": [91, 92, 93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.filter.mathstuff import intersect
from ansible.module_utils.common._collections_compat import Hashable

@pytest.fixture
def mock_environment():
    return Mock()

def test_intersect_with_hashable(mock_environment):
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = intersect(mock_environment, a, b)
    assert result == {2, 3}

def test_intersect_with_non_hashable(mock_environment):
    a = [1, 2, 3]
    b = [2, 3, 4]
    with patch('ansible.plugins.filter.mathstuff.unique', return_value=[2, 3]) as mock_unique:
        result = intersect(mock_environment, a, b)
        mock_unique.assert_called_once_with(mock_environment, [2, 3], True)
        assert result == [2, 3]
