# file: lib/ansible/plugins/filter/urls.py:42-55
# asked: {"lines": [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "branches": [[44, 45], [44, 46], [46, 47], [46, 51], [51, 52], [51, 53]]}
# gained: {"lines": [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "branches": [[44, 45], [44, 46], [46, 47], [46, 51], [51, 52], [51, 53]]}

import pytest
from ansible.plugins.filter.urls import do_urlencode
from ansible.module_utils.six import iteritems, string_types

def unicode_urlencode(value, for_qs=False):
    # Mock implementation of unicode_urlencode for testing purposes
    if for_qs:
        return str(value).replace(' ', '+')
    return str(value)

@pytest.fixture
def mock_unicode_urlencode(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', unicode_urlencode)

def test_do_urlencode_dict(mock_unicode_urlencode):
    value = {'key1': 'value1', 'key2': 'value2'}
    result = do_urlencode(value)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_non_string_iterable(mock_unicode_urlencode):
    value = [('key1', 'value1'), ('key2', 'value2')]
    result = do_urlencode(value)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_string(mock_unicode_urlencode):
    value = 'simple_string'
    result = do_urlencode(value)
    assert result == 'simple_string'

def test_do_urlencode_non_iterable(mock_unicode_urlencode):
    value = 12345
    result = do_urlencode(value)
    assert result == '12345'

def test_do_urlencode_non_iterable_type_error(mock_unicode_urlencode):
    class NonIterable:
        pass

    value = NonIterable()
    result = do_urlencode(value)
    assert result == str(value)
