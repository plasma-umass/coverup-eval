# file lib/ansible/plugins/filter/urls.py:58-69
# lines [62, 63, 66, 67, 69]
# branches ['66->67', '66->69']

import pytest
from unittest.mock import patch

# Assuming the functions do_urldecode and do_urlencode are defined somewhere in the module
def do_urldecode(value):
    pass

def do_urlencode(value):
    pass

# Mocking HAS_URLENCODE to test both branches
@pytest.fixture
def mock_has_urlencode_true(mocker):
    mocker.patch('ansible.plugins.filter.urls.HAS_URLENCODE', True)

@pytest.fixture
def mock_has_urlencode_false(mocker):
    mocker.patch('ansible.plugins.filter.urls.HAS_URLENCODE', False)

def test_filters_with_urlencode(mock_has_urlencode_true):
    from ansible.plugins.filter.urls import FilterModule
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' not in filters

def test_filters_without_urlencode(mock_has_urlencode_false):
    from ansible.plugins.filter.urls import FilterModule
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
