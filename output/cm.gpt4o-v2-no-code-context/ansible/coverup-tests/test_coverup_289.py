# file: lib/ansible/module_utils/facts/system/apparmor.py:26-39
# asked: {"lines": [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39], "branches": [[33, 34], [33, 36]]}
# gained: {"lines": [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39], "branches": [[33, 34], [33, 36]]}

import os
import pytest
from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        if path == '/sys/kernel/security/apparmor':
            return True
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_os_path_not_exists(monkeypatch):
    def mock_exists(path):
        if path == '/sys/kernel/security/apparmor':
            return False
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)

def test_collect_apparmor_enabled(mock_os_path_exists):
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert 'apparmor' in facts
    assert facts['apparmor']['status'] == 'enabled'

def test_collect_apparmor_disabled(mock_os_path_not_exists):
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert 'apparmor' in facts
    assert facts['apparmor']['status'] == 'disabled'
