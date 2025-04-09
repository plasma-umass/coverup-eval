# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [40, 41], "branches": []}
# gained: {"lines": [40, 41], "branches": []}

import pytest
import getpass
import os
import pwd
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_getuser(monkeypatch):
    def mock_getuser():
        return "testuser"
    monkeypatch.setattr(getpass, "getuser", mock_getuser)

@pytest.fixture
def mock_pwd_getpwnam(monkeypatch):
    class MockPwEnt:
        pw_uid = 1001
        pw_gid = 1001
        pw_gecos = "Test User"
        pw_dir = "/home/testuser"
        pw_shell = "/bin/bash"
    
    def mock_getpwnam(username):
        if username == "testuser":
            return MockPwEnt()
        raise KeyError
    
    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)

@pytest.fixture
def mock_pwd_getpwuid(monkeypatch):
    class MockPwEnt:
        pw_uid = 1001
        pw_gid = 1001
        pw_gecos = "Test User"
        pw_dir = "/home/testuser"
        pw_shell = "/bin/bash"
    
    def mock_getpwuid(uid):
        return MockPwEnt()
    
    monkeypatch.setattr(pwd, "getpwuid", mock_getpwuid)

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr(os, "getuid", lambda: 1001)
    monkeypatch.setattr(os, "geteuid", lambda: 1001)
    monkeypatch.setattr(os, "getgid", lambda: 1001)

def test_collect_user_facts(mock_getpass_getuser, mock_pwd_getpwnam, mock_os):
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == "testuser"
    assert facts['user_uid'] == 1001
    assert facts['user_gid'] == 1001
    assert facts['user_gecos'] == "Test User"
    assert facts['user_dir'] == "/home/testuser"
    assert facts['user_shell'] == "/bin/bash"
    assert facts['real_user_id'] == 1001
    assert facts['effective_user_id'] == 1001
    assert facts['real_group_id'] == 1001
    assert facts['effective_group_id'] == 1001

def test_collect_user_facts_keyerror(mock_getpass_getuser, mock_pwd_getpwuid, mock_os, monkeypatch):
    def mock_getpwnam(username):
        raise KeyError
    
    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)
    
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == "testuser"
    assert facts['user_uid'] == 1001
    assert facts['user_gid'] == 1001
    assert facts['user_gecos'] == "Test User"
    assert facts['user_dir'] == "/home/testuser"
    assert facts['user_shell'] == "/bin/bash"
    assert facts['real_user_id'] == 1001
    assert facts['effective_user_id'] == 1001
    assert facts['real_group_id'] == 1001
    assert facts['effective_group_id'] == 1001
