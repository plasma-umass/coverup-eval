# file lib/ansible/module_utils/facts/system/fips.py:26-37
# lines [26, 27, 28, 30, 32, 33, 34, 35, 36, 37]
# branches ['35->36', '35->37']

import pytest
from ansible.module_utils.facts.system.fips import FipsFactCollector

# Mock the function get_file_content to control its behavior in tests
@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.fips.get_file_content')

# Test when /proc/sys/crypto/fips_enabled contains '1'
def test_collect_fips_enabled(mock_get_file_content):
    # Set up the mock to return '1' indicating FIPS is enabled
    mock_get_file_content.return_value = '1'
    
    collector = FipsFactCollector()
    result = collector.collect()
    
    # Assert that the fips fact is set to True
    assert result['fips'] is True

# Test when /proc/sys/crypto/fips_enabled does not contain '1'
def test_collect_fips_disabled(mock_get_file_content):
    # Set up the mock to return '0' indicating FIPS is disabled
    mock_get_file_content.return_value = '0'
    
    collector = FipsFactCollector()
    result = collector.collect()
    
    # Assert that the fips fact is set to False
    assert result['fips'] is False
