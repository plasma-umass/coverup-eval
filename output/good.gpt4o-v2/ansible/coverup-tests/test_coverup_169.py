# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}

import getpass
import os
import pwd
import pytest
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_getuser(monkeypatch):
    def mock_getuser():
        return 'testuser'
    monkeypatch.setattr(getpass, 'getuser', mock_getuser)

@pytest.fixture
def mock_pwd_getpwnam(monkeypatch):
    class MockPwEnt:
        pw_uid = 1000
        pw_gid = 1000
        pw_gecos = 'Test User'
        pw_dir = '/home/testuser'
        pw_shell = '/bin/bash'
    
    def mock_getpwnam(username):
        if username == 'testuser':
            return MockPwEnt()
        raise KeyError
    
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)

@pytest.fixture
def mock_os_functions(monkeypatch):
    monkeypatch.setattr(os, 'getuid', lambda: 1000)
    monkeypatch.setattr(os, 'geteuid', lambda: 1000)
    monkeypatch.setattr(os, 'getgid', lambda: 1000)

def test_collect_user_facts(mock_getpass_getuser, mock_pwd_getpwnam, mock_os_functions):
    collector = UserFactCollector()
    user_facts = collector.collect()
    
    assert user_facts['user_id'] == 'testuser'
    assert user_facts['user_uid'] == 1000
    assert user_facts['user_gid'] == 1000
    assert user_facts['user_gecos'] == 'Test User'
    assert user_facts['user_dir'] == '/home/testuser'
    assert user_facts['user_shell'] == '/bin/bash'
    assert user_facts['real_user_id'] == 1000
    assert user_facts['effective_user_id'] == 1000
    assert user_facts['real_group_id'] == 1000
    assert user_facts['effective_group_id'] == 1000

@pytest.fixture
def mock_pwd_getpwuid(monkeypatch):
    class MockPwEnt:
        pw_uid = 1001
        pw_gid = 1001
        pw_gecos = 'Fallback User'
        pw_dir = '/home/fallbackuser'
        pw_shell = '/bin/sh'
    
    def mock_getpwuid(uid):
        return MockPwEnt()
    
    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)

def test_collect_user_facts_keyerror(mock_getpass_getuser, mock_pwd_getpwuid, mock_os_functions, monkeypatch):
    def mock_getpwnam(username):
        raise KeyError
    
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    
    collector = UserFactCollector()
    user_facts = collector.collect()
    
    assert user_facts['user_id'] == 'testuser'
    assert user_facts['user_uid'] == 1001
    assert user_facts['user_gid'] == 1001
    assert user_facts['user_gecos'] == 'Fallback User'
    assert user_facts['user_dir'] == '/home/fallbackuser'
    assert user_facts['user_shell'] == '/bin/sh'
    assert user_facts['real_user_id'] == 1000
    assert user_facts['effective_user_id'] == 1000
    assert user_facts['real_group_id'] == 1000
    assert user_facts['effective_group_id'] == 1000
