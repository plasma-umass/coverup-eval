# file: lib/ansible/module_utils/common/collections.py:100-112
# asked: {"lines": [100, 107, 108, 109, 110, 111, 112], "branches": [[107, 108], [107, 109], [110, 111], [110, 112]]}
# gained: {"lines": [100, 107, 108, 109, 110, 111, 112], "branches": [[107, 108], [107, 109], [110, 111], [110, 112]]}

import pytest
from ansible.module_utils.common.collections import count

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def test_count_with_iterable():
    seq = [1, 2, 2, 3, 3, 3]
    result = count(seq)
    assert result == {1: 1, 2: 2, 3: 3}

def test_count_with_non_iterable():
    with pytest.raises(Exception, match='Argument provided  is not an iterable'):
        count(123)

def test_count_with_empty_iterable():
    seq = []
    result = count(seq)
    assert result == {}

def test_count_with_string(monkeypatch):
    def mock_is_iterable(obj):
        return True
    monkeypatch.setattr('ansible.module_utils.common.collections.is_iterable', mock_is_iterable)
    seq = "aabbcc"
    result = count(seq)
    assert result == {'a': 2, 'b': 2, 'c': 2}
