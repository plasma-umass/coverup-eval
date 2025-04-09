# file: lib/ansible/plugins/filter/urls.py:58-69
# asked: {"lines": [58, 59, 61, 62, 63, 66, 67, 69], "branches": [[66, 67], [66, 69]]}
# gained: {"lines": [58, 59, 61, 62, 63, 66, 67, 69], "branches": [[66, 67], [66, 69]]}

import pytest
from ansible.plugins.filter.urls import FilterModule, HAS_URLENCODE, do_urldecode, do_urlencode

@pytest.fixture
def filter_module():
    return FilterModule()

def test_filters_with_urlencode(monkeypatch, filter_module):
    monkeypatch.setattr('ansible.plugins.filter.urls.HAS_URLENCODE', True)
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    assert 'urlencode' not in filters

def test_filters_without_urlencode(monkeypatch, filter_module):
    monkeypatch.setattr('ansible.plugins.filter.urls.HAS_URLENCODE', False)
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    assert 'urlencode' in filters
    assert filters['urlencode'] == do_urlencode
