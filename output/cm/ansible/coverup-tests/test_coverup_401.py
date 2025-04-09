# file lib/ansible/module_utils/common/collections.py:100-112
# lines [100, 107, 108, 109, 110, 111, 112]
# branches ['107->108', '107->109', '110->111', '110->112']

import pytest
from ansible.module_utils.common.collections import count

def test_count_with_non_iterable(mocker):
    mocker.patch('ansible.module_utils.common.collections.is_iterable', return_value=False)
    with pytest.raises(Exception) as excinfo:
        count(123)
    assert str(excinfo.value) == 'Argument provided  is not an iterable'

def test_count_with_iterable(mocker):
    mocker.patch('ansible.module_utils.common.collections.is_iterable', return_value=True)
    result = count([1, 2, 2, 3, 3, 3])
    assert result == {1: 1, 2: 2, 3: 3}
