# file: lib/ansible/module_utils/facts/system/apparmor.py:26-39
# asked: {"lines": [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39], "branches": [[33, 34], [33, 36]]}
# gained: {"lines": [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39], "branches": [[33, 34], [33, 36]]}

import os
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector

@pytest.fixture
def apparmor_collector():
    return ApparmorFactCollector()

def test_collect_apparmor_enabled(apparmor_collector, monkeypatch):
    def mock_exists(path):
        return path == '/sys/kernel/security/apparmor'
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    result = apparmor_collector.collect()
    assert result == {'apparmor': {'status': 'enabled'}}

def test_collect_apparmor_disabled(apparmor_collector, monkeypatch):
    def mock_exists(path):
        return False
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    result = apparmor_collector.collect()
    assert result == {'apparmor': {'status': 'disabled'}}
