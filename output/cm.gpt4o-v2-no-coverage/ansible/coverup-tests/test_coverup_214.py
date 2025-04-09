# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}

import pytest
import getpass
import os
import pwd
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
def mock_pwd_getpwuid(monkeypatch):
    class MockPwEnt:
        pw_uid = 1000
        pw_gid = 1000
        pw_gecos = 'Test User'
        pw_dir = '/home/testuser'
        pw_shell = '/bin/bash'
    def mock_getpwuid(uid):
        if uid == 1000:
            return MockPwEnt()
        raise KeyError
    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)

@pytest.fixture
def mock_os_getuid(monkeypatch):
    def mock_getuid():
        return 1000
    monkeypatch.setattr(os, 'getuid', mock_getuid)

@pytest.fixture
def mock_os_geteuid(monkeypatch):
    def mock_geteuid():
        return 1000
    monkeypatch.setattr(os, 'geteuid', mock_geteuid)

@pytest.fixture
def mock_os_getgid(monkeypatch):
    def mock_getgid():
        return 1000
    monkeypatch.setattr(os, 'getgid', mock_getgid)

def test_collect_user_facts(mock_getpass_getuser, mock_pwd_getpwnam, mock_pwd_getpwuid, mock_os_getuid, mock_os_geteuid, mock_os_getgid):
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
