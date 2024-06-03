# file lib/ansible/plugins/filter/core.py:308-338
# lines [309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338]
# branches ['311->312', '311->315', '320->321', '320->323', '323->324', '323->333', '335->336', '335->338']

import pytest
from ansible.plugins.filter.core import combine, AnsibleFilterError

def test_combine_no_kwargs():
    assert combine() == {}

def test_combine_single_dict():
    assert combine({'a': 1}) == {'a': 1}

def test_combine_multiple_dicts():
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}
    assert combine({'a': 1}, {'a': 2}) == {'a': 2}

def test_combine_recursive(mocker):
    mocker.patch('ansible.plugins.filter.core.merge_hash', side_effect=lambda d1, d2, recursive, list_merge: {**d1, **d2} if not recursive else {k: {**d1.get(k, {}), **d2.get(k, {})} for k in set(d1) | set(d2)})
    assert combine({'a': {'b': 1}}, {'a': {'c': 2}}, recursive=True) == {'a': {'b': 1, 'c': 2}}

def test_combine_list_merge():
    assert combine({'a': [1, 2]}, {'a': [3, 4]}, list_merge='replace') == {'a': [3, 4]}

def test_combine_invalid_kwargs():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine({'a': 1}, invalid_kwarg=True)

def test_combine_empty_dicts():
    assert combine({}, {}) == {}

def test_combine_mixed_dicts():
    assert combine({'a': 1}, {}, {'b': 2}) == {'a': 1, 'b': 2}

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.patch('ansible.plugins.filter.core.flatten', side_effect=lambda x, levels: x)
    mocker.patch('ansible.plugins.filter.core.recursive_check_defined', return_value=None)
    yield
