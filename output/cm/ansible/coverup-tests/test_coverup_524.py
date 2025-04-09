# file lib/ansible/module_utils/facts/other/facter.py:36-44
# lines [36, 37, 38, 41, 42, 44]
# branches ['41->42', '41->44']

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from unittest.mock import MagicMock

@pytest.fixture
def mock_module(mocker):
    module = MagicMock()
    module.get_bin_path = MagicMock(side_effect=lambda bin_name, opt_dirs: '/opt/puppetlabs/bin/cfacter' if bin_name == 'cfacter' else '/usr/bin/facter')
    return module

def test_find_facter_with_cfacter(mock_module):
    fact_collector = FacterFactCollector()
    facter_path = fact_collector.find_facter(mock_module)
    assert facter_path == '/opt/puppetlabs/bin/cfacter'

def test_find_facter_without_cfacter(mock_module):
    mock_module.get_bin_path.side_effect = lambda bin_name, opt_dirs: None if bin_name == 'cfacter' else '/usr/bin/facter'
    fact_collector = FacterFactCollector()
    facter_path = fact_collector.find_facter(mock_module)
    assert facter_path == '/usr/bin/facter'
