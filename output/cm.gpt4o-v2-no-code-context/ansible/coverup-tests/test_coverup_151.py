# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}

import pytest
import getpass
import pwd
import os
from ansible.module_utils.facts.system.user import UserFactCollector

class MockPwent:
    def __init__(self, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell):
        self.pw_uid = pw_uid
        self.pw_gid = pw_gid
        self.pw_gecos = pw_gecos
        self.pw_dir = pw_dir
        self.pw_shell = pw_shell

@pytest.fixture
def mock_getpwnam(monkeypatch):
    def mock_getpwnam(username):
        if username == 'existing_user':
            return MockPwent(1000, 1000, 'Existing User', '/home/existing_user', '/bin/bash')
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)

@pytest.fixture
def mock_getpass_getuser(monkeypatch):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'existing_user')

@pytest.fixture
def mock_os_functions(monkeypatch):
    monkeypatch.setattr(os, 'getuid', lambda: 1000)
    monkeypatch.setattr(os, 'geteuid', lambda: 1000)
    monkeypatch.setattr(os, 'getgid', lambda: 1000)

def test_collect_existing_user(mock_getpwnam, mock_getpass_getuser, mock_os_functions):
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == 'existing_user'
    assert facts['user_uid'] == 1000
    assert facts['user_gid'] == 1000
    assert facts['user_gecos'] == 'Existing User'
    assert facts['user_dir'] == '/home/existing_user'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == 1000
    assert facts['effective_user_id'] == 1000
    assert facts['real_group_id'] == 1000
    assert facts['effective_group_id'] == 1000

@pytest.fixture
def mock_getpwnam_keyerror(monkeypatch):
    def mock_getpwnam(username):
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)

@pytest.fixture
def mock_getpwuid(monkeypatch):
    def mock_getpwuid(uid):
        return MockPwent(1000, 1000, 'UID User', '/home/uid_user', '/bin/sh')

    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)

def test_collect_keyerror(mock_getpwnam_keyerror, mock_getpwuid, mock_getpass_getuser, mock_os_functions):
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == 'existing_user'
    assert facts['user_uid'] == 1000
    assert facts['user_gid'] == 1000
    assert facts['user_gecos'] == 'UID User'
    assert facts['user_dir'] == '/home/uid_user'
    assert facts['user_shell'] == '/bin/sh'
    assert facts['real_user_id'] == 1000
    assert facts['effective_user_id'] == 1000
    assert facts['real_group_id'] == 1000
    assert facts['effective_group_id'] == 1000
