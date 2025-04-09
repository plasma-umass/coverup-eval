# file lib/ansible/module_utils/facts/system/selinux.py:40-91
# lines [71, 86]
# branches ['68->71', '83->86']

import pytest
from unittest.mock import patch, MagicMock

# Import the necessary module and class
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

@pytest.fixture
def selinux_mock():
    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False):
        with patch('ansible.module_utils.facts.system.selinux.selinux') as mock_selinux:
            yield mock_selinux

def test_selinux_fact_collector_missing_library(selinux_mock):
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert facts['selinux']['status'] == 'Missing selinux Python library'
    assert facts['selinux_python_present'] == False

def test_selinux_fact_collector_config_mode_unknown(selinux_mock):
    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True):
        selinux_mock.is_selinux_enabled.return_value = True
        selinux_mock.security_policyvers.return_value = 30
        selinux_mock.selinux_getenforcemode.return_value = (1, None)  # Simulate non-zero return code
        selinux_mock.security_getenforce.return_value = 1
        selinux_mock.selinux_getpolicytype.return_value = (0, 'targeted')

        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['config_mode'] == 'unknown'

def test_selinux_fact_collector_type_unknown(selinux_mock):
    with patch('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True):
        selinux_mock.is_selinux_enabled.return_value = True
        selinux_mock.security_policyvers.return_value = 30
        selinux_mock.selinux_getenforcemode.return_value = (0, 1)
        selinux_mock.security_getenforce.return_value = 1
        selinux_mock.selinux_getpolicytype.return_value = (1, None)  # Simulate non-zero return code

        collector = SelinuxFactCollector()
        facts = collector.collect()
        assert facts['selinux']['type'] == 'unknown'
