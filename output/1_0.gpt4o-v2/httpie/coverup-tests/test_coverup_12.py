# file: httpie/cli/dicts.py:17-42
# asked: {"lines": [17, 18, 20, 29, 30, 31, 33, 34, 35, 37, 38, 39, 40, 41, 42], "branches": [[30, 31], [30, 33], [33, 34], [33, 35], [38, 0], [38, 39], [39, 40], [39, 41], [41, 38], [41, 42]]}
# gained: {"lines": [17, 18, 20, 29, 30, 31, 33, 34, 35, 37, 38, 39, 40, 41, 42], "branches": [[30, 31], [30, 33], [33, 34], [38, 0], [38, 39], [39, 40], [39, 41], [41, 38], [41, 42]]}

import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_setitem_single_value():
    d = MultiValueOrderedDict()
    d['key'] = 'value'
    assert d['key'] == 'value'

def test_setitem_multiple_values():
    d = MultiValueOrderedDict()
    d['key'] = 'value1'
    d['key'] = 'value2'
    assert d['key'] == ['value1', 'value2']

def test_setitem_assert_not_list():
    d = MultiValueOrderedDict()
    with pytest.raises(AssertionError):
        d['key'] = ['value']

def test_items_single_value():
    d = MultiValueOrderedDict()
    d['key'] = 'value'
    items = list(d.items())
    assert items == [('key', 'value')]

def test_items_multiple_values():
    d = MultiValueOrderedDict()
    d['key'] = 'value1'
    d['key'] = 'value2'
    items = list(d.items())
    assert items == [('key', 'value1'), ('key', 'value2')]
