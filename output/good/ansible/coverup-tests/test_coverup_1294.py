# file lib/ansible/module_utils/facts/system/selinux.py:40-91
# lines [48, 49, 50, 51, 71, 86]
# branches ['47->48', '68->71', '83->86']

import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
from unittest.mock import MagicMock, patch

SELINUX_MODE_DICT = {
    0: 'enforcing',
    1: 'permissive',
    2: 'disabled'
}

# Mock selinux module to simulate different conditions
class MockSelinuxModule:
    @staticmethod
    def is_selinux_enabled():
        return True

    @staticmethod
    def security_policyvers():
        raise AttributeError

    @staticmethod
    def selinux_getenforcemode():
        return (1, None)  # Simulate failure to get enforce mode

    @staticmethod
    def security_getenforce():
        return 0  # enforcing

    @staticmethod
    def selinux_getpolicytype():
        return (1, None)  # Simulate failure to get policy type

@pytest.fixture
def selinux_not_present(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False)

@pytest.fixture
def selinux_present(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.selinux', MockSelinuxModule)
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.SELINUX_MODE_DICT', SELINUX_MODE_DICT)

def test_selinux_facts_with_missing_library(selinux_not_present):
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert facts['selinux']['status'] == 'Missing selinux Python library'
    assert facts['selinux_python_present'] == False

def test_selinux_facts_with_present_library(selinux_present):
    collector = SelinuxFactCollector()
    facts = collector.collect()
    assert facts['selinux_python_present'] == True
    assert facts['selinux']['status'] == 'enabled'
    assert facts['selinux']['policyvers'] == 'unknown'
    assert facts['selinux']['config_mode'] == 'unknown'
    assert facts['selinux']['mode'] == 'enforcing'
    assert facts['selinux']['type'] == 'unknown'
