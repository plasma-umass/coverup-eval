# file lib/ansible/module_utils/facts/system/selinux.py:40-91
# lines [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 90, 91]
# branches ['47->48', '47->54', '56->57', '56->59', '68->69', '68->71', '83->84', '83->86']

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

SELINUX_MODE_DICT = {1: 'enforcing', 0: 'permissive', -1: 'disabled'}

@pytest.fixture
def selinux_mock(mocker):
    selinux = mocker.patch('ansible.module_utils.facts.system.selinux.selinux')
    return selinux

def test_selinux_fact_collector_with_selinux_disabled(selinux_mock):
    selinux_mock.is_selinux_enabled.return_value = False
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert facts['selinux']['status'] == 'disabled'
    assert facts['selinux_python_present'] is True

def test_selinux_fact_collector_with_selinux_enabled_and_exceptions(selinux_mock):
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.side_effect = AttributeError
    selinux_mock.selinux_getenforcemode.side_effect = OSError
    selinux_mock.security_getenforce.side_effect = AttributeError
    selinux_mock.selinux_getpolicytype.side_effect = OSError

    collector = SelinuxFactCollector()
    facts = collector.collect()

    assert facts['selinux']['status'] == 'enabled'
    assert facts['selinux']['policyvers'] == 'unknown'
    assert facts['selinux']['config_mode'] == 'unknown'
    assert facts['selinux']['mode'] == 'unknown'
    assert facts['selinux']['type'] == 'unknown'
    assert facts['selinux_python_present'] is True

def test_selinux_fact_collector_with_selinux_enabled_and_valid_values(selinux_mock):
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.return_value = 30
    selinux_mock.selinux_getenforcemode.return_value = (0, 1)
    selinux_mock.security_getenforce.return_value = 0
    selinux_mock.selinux_getpolicytype.return_value = (0, 'targeted')

    collector = SelinuxFactCollector()
    facts = collector.collect()

    assert facts['selinux']['status'] == 'enabled'
    assert facts['selinux']['policyvers'] == 30
    assert facts['selinux']['config_mode'] == 'enforcing'
    assert facts['selinux']['mode'] == 'permissive'
    assert facts['selinux']['type'] == 'targeted'
    assert facts['selinux_python_present'] is True
