# file lib/ansible/plugins/filter/urls.py:58-69
# lines [58, 59, 61, 62, 63, 66, 67, 69]
# branches ['66->67', '66->69']

import pytest
from ansible.plugins.filter.urls import FilterModule

# Mocking the HAS_URLENCODE variable to simulate the environment where it's False
@pytest.fixture
def mock_has_urlencode(mocker):
    mocker.patch('ansible.plugins.filter.urls.HAS_URLENCODE', False)

# Test function to cover the branch where HAS_URLENCODE is False
def test_filter_module_without_urlencode(mock_has_urlencode):
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters  # This line should now be covered
    # You can add more assertions here to check the correct behavior of the filters
