# file lib/ansible/plugins/filter/mathstuff.py:109-116
# lines [111, 112, 114, 115, 116]
# branches ['111->112', '111->114']

import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference

def test_symmetric_difference_hashable(mocker):
    environment = mocker.Mock()
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])
    result = symmetric_difference(environment, a, b)
    assert result == {1, 2, 4, 5}

def test_symmetric_difference_non_hashable(mocker):
    environment = mocker.Mock()
    a = [1, 2, 3]
    b = [3, 4, 5]
    
    mocker.patch('ansible.plugins.filter.mathstuff.intersect', return_value=[3])
    mocker.patch('ansible.plugins.filter.mathstuff.union', return_value=[1, 2, 3, 4, 5])
    
    result = symmetric_difference(environment, a, b)
    assert result == [1, 2, 4, 5]
