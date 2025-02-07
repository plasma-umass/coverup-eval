# file: lib/ansible/module_utils/facts/system/fips.py:26-37
# asked: {"lines": [32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.fips import FipsFactCollector

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.fips.get_file_content') as mock:
        yield mock

def test_fips_fact_collector_fips_enabled(mock_get_file_content):
    mock_get_file_content.return_value = '1'
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': True}

def test_fips_fact_collector_fips_disabled(mock_get_file_content):
    mock_get_file_content.return_value = '0'
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}

def test_fips_fact_collector_no_file(mock_get_file_content):
    mock_get_file_content.return_value = None
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}
