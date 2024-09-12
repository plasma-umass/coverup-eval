# file: lib/ansible/plugins/filter/core.py:308-338
# asked: {"lines": [309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}
# gained: {"lines": [309, 310, 311, 312, 315, 318, 320, 321, 323, 324, 333, 334, 335, 336, 338], "branches": [[311, 312], [311, 315], [320, 321], [320, 323], [323, 324], [323, 333], [335, 336], [335, 338]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import combine

def test_combine_no_kwargs():
    assert combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_combine_recursive():
    assert combine({'a': {'b': 1}}, {'a': {'c': 2}}, recursive=True) == {'a': {'b': 1, 'c': 2}}

def test_combine_list_merge_replace():
    assert combine({'a': [1, 2]}, {'a': [3, 4]}, list_merge='replace') == {'a': [3, 4]}

def test_combine_list_merge_append():
    assert combine({'a': [1, 2]}, {'a': [3, 4]}, list_merge='append') == {'a': [1, 2, 3, 4]}

def test_combine_list_merge_prepend():
    assert combine({'a': [1, 2]}, {'a': [3, 4]}, list_merge='prepend') == {'a': [3, 4, 1, 2]}

def test_combine_invalid_kwargs():
    with pytest.raises(AnsibleFilterError, match="'recursive' and 'list_merge' are the only valid keyword arguments"):
        combine({'a': 1}, invalid_kwarg=True)

def test_combine_empty():
    assert combine() == {}

def test_combine_single_dict():
    assert combine({'a': 1}) == {'a': 1}
