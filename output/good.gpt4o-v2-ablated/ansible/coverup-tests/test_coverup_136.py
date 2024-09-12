# file: lib/ansible/module_utils/facts/system/fips.py:26-37
# asked: {"lines": [26, 27, 28, 30, 32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}
# gained: {"lines": [26, 27, 28, 30, 32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}

import pytest
from unittest.mock import patch, mock_open

# Assuming the FipsFactCollector and get_file_content are imported from the module
from ansible.module_utils.facts.system.fips import FipsFactCollector, get_file_content

@pytest.fixture
def fips_collector():
    return FipsFactCollector()

def test_collect_fips_disabled(fips_collector, monkeypatch):
    # Mock get_file_content to return '0'
    monkeypatch.setattr('ansible.module_utils.facts.system.fips.get_file_content', lambda x: '0')
    
    result = fips_collector.collect()
    assert result == {'fips': False}

def test_collect_fips_enabled(fips_collector, monkeypatch):
    # Mock get_file_content to return '1'
    monkeypatch.setattr('ansible.module_utils.facts.system.fips.get_file_content', lambda x: '1')
    
    result = fips_collector.collect()
    assert result == {'fips': True}

def test_collect_fips_no_data(fips_collector, monkeypatch):
    # Mock get_file_content to return None
    monkeypatch.setattr('ansible.module_utils.facts.system.fips.get_file_content', lambda x: None)
    
    result = fips_collector.collect()
    assert result == {'fips': False}
