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

def test_combine_recursive():
    assert combine({'a': {'b': 1}}, {'a': {'c': 2}}, recursive=True) == {'a': {'b': 1, 'c': 2}}

def test_combine_list_merge():
    assert combine({'a': [1, 2]}, {'a': [3, 4]}, list_merge='append') == {'a': [1, 2, 3, 4]}

def test_combine_invalid_kwargs():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine({'a': 1}, invalid_kwarg=True)

def test_combine_empty_dicts():
    assert combine({}, {}) == {}

def test_combine_with_flatten(monkeypatch):
    def mock_flatten(terms, levels):
        return terms
    monkeypatch.setattr('ansible.plugins.filter.core.flatten', mock_flatten)
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_combine_with_recursive_check_defined(monkeypatch):
    def mock_recursive_check_defined(dictionaries):
        pass
    monkeypatch.setattr('ansible.plugins.filter.core.recursive_check_defined', mock_recursive_check_defined)
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_combine_with_merge_hash(monkeypatch):
    def mock_merge_hash(dict1, dict2, recursive, list_merge):
        return {**dict1, **dict2}
    monkeypatch.setattr('ansible.plugins.filter.core.merge_hash', mock_merge_hash)
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}
