# file: httpie/cli/dicts.py:17-42
# asked: {"lines": [], "branches": [[33, 35]]}
# gained: {"lines": [], "branches": [[33, 35]]}

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

def test_setitem_append_to_list():
    d = MultiValueOrderedDict()
    d['key'] = 'value1'
    d['key'] = 'value2'
    d['key'] = 'value3'
    assert d['key'] == ['value1', 'value2', 'value3']

def test_setitem_no_list_as_value():
    d = MultiValueOrderedDict()
    with pytest.raises(AssertionError):
        d['key'] = ['value1', 'value2']
