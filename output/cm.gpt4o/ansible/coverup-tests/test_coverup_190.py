# file lib/ansible/module_utils/facts/system/user.py:26-53
# lines [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53]
# branches []

import pytest
import getpass
import pwd
import os
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_getuser(mocker):
    return mocker.patch('getpass.getuser', return_value='testuser')

@pytest.fixture
def mock_pwd_getpwnam(mocker):
    pwent = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    return mocker.patch('pwd.getpwnam', return_value=pwent)

@pytest.fixture
def mock_pwd_getpwuid(mocker):
    pwent = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    return mocker.patch('pwd.getpwuid', return_value=pwent)

@pytest.fixture
def mock_os_getuid(mocker):
    return mocker.patch('os.getuid', return_value=1001)

@pytest.fixture
def mock_os_geteuid(mocker):
    return mocker.patch('os.geteuid', return_value=1001)

@pytest.fixture
def mock_os_getgid(mocker):
    return mocker.patch('os.getgid', return_value=1001)

def test_user_fact_collector(mock_getpass_getuser, mock_pwd_getpwnam, mock_pwd_getpwuid, mock_os_getuid, mock_os_geteuid, mock_os_getgid):
    collector = UserFactCollector()
    facts = collector.collect()

    assert facts['user_id'] == 'testuser'
    assert facts['user_uid'] == 1001
    assert facts['user_gid'] == 1001
    assert facts['user_gecos'] == 'Test User'
    assert facts['user_dir'] == '/home/testuser'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == 1001
    assert facts['effective_user_id'] == 1001
    assert facts['real_group_id'] == 1001
    assert facts['effective_group_id'] == 1001
