# file: lib/ansible/plugins/filter/core.py:308-338
# asked: {"lines": [308, 309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}
# gained: {"lines": [308, 309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import combine

def test_combine_no_terms():
    assert combine() == {}

def test_combine_single_term():
    assert combine({'a': 1}) == {'a': 1}

def test_combine_multiple_terms():
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_combine_recursive_kwarg():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine({'a': 1}, recursive=True, invalid_kwarg=True)

def test_combine_list_merge_kwarg():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine({'a': 1}, list_merge='append', invalid_kwarg=True)

def test_combine_recursive_merge(mocker):
    mocker.patch('ansible.plugins.filter.core.merge_hash', side_effect=lambda x, y, r, l: {**x, **y})
    result = combine({'a': 1}, {'b': 2}, recursive=True)
    assert result == {'a': 1, 'b': 2}

def test_combine_list_merge_replace(mocker):
    mocker.patch('ansible.plugins.filter.core.merge_hash', side_effect=lambda x, y, r, l: {**x, **y})
    result = combine({'a': 1, 'list': [1, 2]}, {'b': 2, 'list': [3, 4]}, list_merge='replace')
    assert result == {'a': 1, 'b': 2, 'list': [3, 4]}

def test_combine_list_merge_append(mocker):
    mocker.patch('ansible.plugins.filter.core.merge_hash', side_effect=lambda x, y, r, l: {**x, **y, 'list': x.get('list', []) + y.get('list', [])})
    result = combine({'a': 1, 'list': [1, 2]}, {'b': 2, 'list': [3, 4]}, list_merge='append')
    assert result == {'a': 1, 'b': 2, 'list': [1, 2, 3, 4]}
