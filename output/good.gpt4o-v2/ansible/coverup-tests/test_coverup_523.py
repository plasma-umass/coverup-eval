# file: lib/ansible/module_utils/facts/other/facter.py:36-44
# asked: {"lines": [36, 37, 38, 41, 42, 44], "branches": [[41, 42], [41, 44]]}
# gained: {"lines": [36, 37, 38, 41, 42, 44], "branches": [[41, 42], [41, 44]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_find_facter_with_cfacter(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path.side_effect = lambda name, opt_dirs: '/opt/puppetlabs/bin/' + name if name == 'cfacter' else None

    facter_path = collector.find_facter(mock_module)

    assert facter_path == '/opt/puppetlabs/bin/cfacter'
    mock_module.get_bin_path.assert_any_call('facter', opt_dirs=['/opt/puppetlabs/bin'])
    mock_module.get_bin_path.assert_any_call('cfacter', opt_dirs=['/opt/puppetlabs/bin'])

def test_find_facter_without_cfacter(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path.side_effect = lambda name, opt_dirs: '/opt/puppetlabs/bin/' + name if name == 'facter' else None

    facter_path = collector.find_facter(mock_module)

    assert facter_path == '/opt/puppetlabs/bin/facter'
    mock_module.get_bin_path.assert_any_call('facter', opt_dirs=['/opt/puppetlabs/bin'])
    mock_module.get_bin_path.assert_any_call('cfacter', opt_dirs=['/opt/puppetlabs/bin'])
