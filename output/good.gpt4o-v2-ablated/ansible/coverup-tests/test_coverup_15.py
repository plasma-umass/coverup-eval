# file: lib/ansible/module_utils/facts/system/selinux.py:40-91
# asked: {"lines": [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 90, 91], "branches": [[47, 48], [47, 54], [56, 57], [56, 59], [68, 69], [68, 71], [83, 84], [83, 86]]}
# gained: {"lines": [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 87, 88, 90, 91], "branches": [[47, 48], [47, 54], [56, 57], [56, 59], [68, 69], [83, 84]]}

import pytest
from unittest.mock import patch, MagicMock

# Mocking the selinux module and constants
selinux_mock = MagicMock()
SELINUX_MODE_DICT = {0: 'permissive', 1: 'enforcing'}

# Import the class to be tested
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

@pytest.fixture
def selinux_collector():
    return SelinuxFactCollector()

def test_collect_no_selinux_library(selinux_collector, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False)
    result = selinux_collector.collect()
    assert result == {
        'selinux': {'status': 'Missing selinux Python library'},
        'selinux_python_present': False
    }

def test_collect_selinux_disabled(selinux_collector, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    monkeypatch.setattr(selinux_mock, 'is_selinux_enabled', lambda: False)
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.selinux', selinux_mock)
    result = selinux_collector.collect()
    assert result == {
        'selinux': {'status': 'disabled'},
        'selinux_python_present': True
    }

def test_collect_selinux_enabled(selinux_collector, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    monkeypatch.setattr(selinux_mock, 'is_selinux_enabled', lambda: True)
    monkeypatch.setattr(selinux_mock, 'security_policyvers', lambda: 30)
    monkeypatch.setattr(selinux_mock, 'selinux_getenforcemode', lambda: (0, 1))
    monkeypatch.setattr(selinux_mock, 'security_getenforce', lambda: 1)
    monkeypatch.setattr(selinux_mock, 'selinux_getpolicytype', lambda: (0, 'targeted'))
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.selinux', selinux_mock)
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.SELINUX_MODE_DICT', SELINUX_MODE_DICT)
    
    result = selinux_collector.collect()
    assert result == {
        'selinux': {
            'status': 'enabled',
            'policyvers': 30,
            'config_mode': 'enforcing',
            'mode': 'enforcing',
            'type': 'targeted'
        },
        'selinux_python_present': True
    }

def test_collect_selinux_enabled_exceptions(selinux_collector, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    monkeypatch.setattr(selinux_mock, 'is_selinux_enabled', lambda: True)
    monkeypatch.setattr(selinux_mock, 'security_policyvers', MagicMock(side_effect=OSError))
    monkeypatch.setattr(selinux_mock, 'selinux_getenforcemode', MagicMock(side_effect=OSError))
    monkeypatch.setattr(selinux_mock, 'security_getenforce', MagicMock(side_effect=OSError))
    monkeypatch.setattr(selinux_mock, 'selinux_getpolicytype', MagicMock(side_effect=OSError))
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.selinux', selinux_mock)
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.SELINUX_MODE_DICT', SELINUX_MODE_DICT)
    
    result = selinux_collector.collect()
    assert result == {
        'selinux': {
            'status': 'enabled',
            'policyvers': 'unknown',
            'config_mode': 'unknown',
            'mode': 'unknown',
            'type': 'unknown'
        },
        'selinux_python_present': True
    }
