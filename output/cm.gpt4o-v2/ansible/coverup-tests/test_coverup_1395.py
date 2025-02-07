# file: lib/ansible/module_utils/facts/system/selinux.py:40-91
# asked: {"lines": [71, 86], "branches": [[68, 71], [83, 86]]}
# gained: {"lines": [71, 86], "branches": [[68, 71], [83, 86]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

@pytest.fixture
def selinux_mock():
    with patch('ansible.module_utils.facts.system.selinux.selinux', autospec=True) as mock_selinux:
        yield mock_selinux

def test_collect_selinux_getenforcemode_failure(selinux_mock):
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.return_value = 30
    selinux_mock.selinux_getenforcemode.return_value = [1, None]  # Simulate failure
    selinux_mock.security_getenforce.return_value = 1
    selinux_mock.selinux_getpolicytype.return_value = [0, 'targeted']

    collector = SelinuxFactCollector()
    facts = collector.collect()

    assert facts['selinux']['config_mode'] == 'unknown'

def test_collect_selinux_getpolicytype_failure(selinux_mock):
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.return_value = 30
    selinux_mock.selinux_getenforcemode.return_value = [0, 1]
    selinux_mock.security_getenforce.return_value = 1
    selinux_mock.selinux_getpolicytype.return_value = [1, None]  # Simulate failure

    collector = SelinuxFactCollector()
    facts = collector.collect()

    assert facts['selinux']['type'] == 'unknown'
