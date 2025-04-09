# file: lib/ansible/module_utils/facts/other/facter.py:36-44
# asked: {"lines": [36, 37, 38, 41, 42, 44], "branches": [[41, 42], [41, 44]]}
# gained: {"lines": [36, 37, 38, 41, 42, 44], "branches": [[41, 42], [41, 44]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_find_facter_with_cfacter(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path = Mock(side_effect=lambda name, opt_dirs: '/opt/puppetlabs/bin/cfacter' if name == 'cfacter' else None)
    
    facter_path = collector.find_facter(mock_module)
    
    assert facter_path == '/opt/puppetlabs/bin/cfacter'

def test_find_facter_with_facter(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path = Mock(side_effect=lambda name, opt_dirs: '/opt/puppetlabs/bin/facter' if name == 'facter' else None)
    
    facter_path = collector.find_facter(mock_module)
    
    assert facter_path == '/opt/puppetlabs/bin/facter'

def test_find_facter_with_both(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path = Mock(side_effect=lambda name, opt_dirs: '/opt/puppetlabs/bin/cfacter' if name == 'cfacter' else '/opt/puppetlabs/bin/facter')
    
    facter_path = collector.find_facter(mock_module)
    
    assert facter_path == '/opt/puppetlabs/bin/cfacter'

def test_find_facter_with_none(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path = Mock(return_value=None)
    
    facter_path = collector.find_facter(mock_module)
    
    assert facter_path is None
