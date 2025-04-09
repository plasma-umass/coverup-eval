# file lib/ansible/module_utils/facts/system/fips.py:26-37
# lines [26, 27, 28, 30, 32, 33, 34, 35, 36, 37]
# branches ['35->36', '35->37']

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.fips import FipsFactCollector

@pytest.fixture
def fips_collector():
    return FipsFactCollector()

def test_fips_enabled(fips_collector):
    with patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='1'):
        result = fips_collector.collect()
        assert result['fips'] is True

def test_fips_disabled(fips_collector):
    with patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='0'):
        result = fips_collector.collect()
        assert result['fips'] is False

def test_fips_no_file(fips_collector):
    with patch('ansible.module_utils.facts.system.fips.get_file_content', return_value=None):
        result = fips_collector.collect()
        assert result['fips'] is False
