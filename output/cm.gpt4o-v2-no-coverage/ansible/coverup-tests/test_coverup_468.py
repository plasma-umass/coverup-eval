# file: lib/ansible/module_utils/common/collections.py:100-112
# asked: {"lines": [100, 107, 108, 109, 110, 111, 112], "branches": [[107, 108], [107, 109], [110, 111], [110, 112]]}
# gained: {"lines": [100, 107, 108, 109, 110, 111, 112], "branches": [[107, 108], [107, 109], [110, 111], [110, 112]]}

import pytest
from ansible.module_utils.common.collections import count
from ansible.module_utils.common.collections import is_iterable

def test_count_with_iterable():
    result = count([1, 2, 2, 3, 3, 3])
    assert result == {1: 1, 2: 2, 3: 3}

def test_count_with_non_iterable():
    with pytest.raises(Exception, match='Argument provided  is not an iterable'):
        count(123)

def test_count_with_empty_iterable():
    result = count([])
    assert result == {}

def test_count_with_strings(monkeypatch):
    def mock_is_iterable(seq, include_strings=False):
        return True

    monkeypatch.setattr('ansible.module_utils.common.collections.is_iterable', mock_is_iterable)
    result = count("aabbcc")
    assert result == {'a': 2, 'b': 2, 'c': 2}
