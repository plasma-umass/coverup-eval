# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}

import getpass
import os
import pwd
import pytest
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_user(mocker):
    return mocker.patch('getpass.getuser', return_value='testuser')

@pytest.fixture
def mock_pwd_getpwnam(mocker):
    pwent = pwd.struct_passwd(('testuser', 'x', 1000, 1000, 'Test User', '/home/testuser', '/bin/bash'))
    return mocker.patch('pwd.getpwnam', return_value=pwent)

@pytest.fixture
def mock_pwd_getpwuid(mocker):
    pwent = pwd.struct_passwd(('testuser', 'x', 1000, 1000, 'Test User', '/home/testuser', '/bin/bash'))
    return mocker.patch('pwd.getpwuid', return_value=pwent)

@pytest.fixture
def mock_os_getuid(mocker):
    return mocker.patch('os.getuid', return_value=1000)

@pytest.fixture
def mock_os_geteuid(mocker):
    return mocker.patch('os.geteuid', return_value=1000)

@pytest.fixture
def mock_os_getgid(mocker):
    return mocker.patch('os.getgid', return_value=1000)

def test_collect_user_facts(mock_getpass_user, mock_pwd_getpwnam, mock_os_getuid, mock_os_geteuid, mock_os_getgid):
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

def test_collect_user_facts_keyerror(mock_getpass_user, mock_pwd_getpwuid, mock_os_getuid, mock_os_geteuid, mock_os_getgid, mocker):
    mocker.patch('pwd.getpwnam', side_effect=KeyError)
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
