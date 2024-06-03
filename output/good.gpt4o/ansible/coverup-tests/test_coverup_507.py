# file lib/ansible/module_utils/facts/other/facter.py:36-44
# lines [36, 37, 38, 41, 42, 44]
# branches ['41->42', '41->44']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_find_facter_with_cfacter(mock_module):
    mock_module.get_bin_path.side_effect = lambda name, opt_dirs: '/opt/puppetlabs/bin/' + name if name == 'cfacter' else None
    collector = FacterFactCollector()
    facter_path = collector.find_facter(mock_module)
    assert facter_path == '/opt/puppetlabs/bin/cfacter'

def test_find_facter_without_cfacter(mock_module):
    mock_module.get_bin_path.side_effect = lambda name, opt_dirs: '/opt/puppetlabs/bin/' + name if name == 'facter' else None
    collector = FacterFactCollector()
    facter_path = collector.find_facter(mock_module)
    assert facter_path == '/opt/puppetlabs/bin/facter'

def test_find_facter_neither(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = FacterFactCollector()
    facter_path = collector.find_facter(mock_module)
    assert facter_path is None
