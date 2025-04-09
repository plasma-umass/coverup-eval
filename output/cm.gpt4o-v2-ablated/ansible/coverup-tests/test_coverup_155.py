# file: lib/ansible/plugins/filter/urls.py:58-69
# asked: {"lines": [58, 59, 61, 62, 63, 66, 67, 69], "branches": [[66, 67], [66, 69]]}
# gained: {"lines": [58, 59, 61, 62, 63, 66, 67, 69], "branches": [[66, 67], [66, 69]]}

import pytest
from ansible.plugins.filter.urls import FilterModule

def test_filters(monkeypatch):
    # Mock the HAS_URLENCODE variable to test both branches
    monkeypatch.setattr('ansible.plugins.filter.urls.HAS_URLENCODE', True)
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' not in filters

    monkeypatch.setattr('ansible.plugins.filter.urls.HAS_URLENCODE', False)
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
