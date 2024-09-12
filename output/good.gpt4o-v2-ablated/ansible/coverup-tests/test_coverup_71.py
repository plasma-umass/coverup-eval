# file: lib/ansible/module_utils/facts/system/user.py:26-53
# asked: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [26, 27, 28, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53], "branches": []}

import pytest
import getpass
import pwd
import os
from ansible.module_utils.facts.system.user import UserFactCollector

@pytest.fixture
def mock_getpass_getuser(mocker):
    mocker.patch('getpass.getuser', return_value='testuser')

@pytest.fixture
def mock_pwd_getpwnam(mocker):
    mock_pwent = mocker.Mock()
    mock_pwent.pw_uid = 1000
    mock_pwent.pw_gid = 1000
    mock_pwent.pw_gecos = 'Test User'
    mock_pwent.pw_dir = '/home/testuser'
    mock_pwent.pw_shell = '/bin/bash'
    mocker.patch('pwd.getpwnam', return_value=mock_pwent)
    return mock_pwent

@pytest.fixture
def mock_pwd_getpwuid(mocker):
    mock_pwent = mocker.Mock()
    mock_pwent.pw_uid = 1001
    mock_pwent.pw_gid = 1001
    mock_pwent.pw_gecos = 'Fallback User'
    mock_pwent.pw_dir = '/home/fallbackuser'
    mock_pwent.pw_shell = '/bin/sh'
    mocker.patch('pwd.getpwuid', return_value=mock_pwent)
    return mock_pwent

@pytest.fixture
def mock_os_functions(mocker):
    mocker.patch('os.getuid', return_value=1000)
    mocker.patch('os.geteuid', return_value=1000)
    mocker.patch('os.getgid', return_value=1000)
    mocker.patch('os.getegid', return_value=1000)

def test_collect_user_facts_success(mock_getpass_getuser, mock_pwd_getpwnam, mock_os_functions):
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == 'testuser'
    assert facts['user_uid'] == 1000
    assert facts['user_gid'] == 1000
    assert facts['user_gecos'] == 'Test User'
    assert facts['user_dir'] == '/home/testuser'
    assert facts['user_shell'] == '/bin/bash'
    assert facts['real_user_id'] == 1000
    assert facts['effective_user_id'] == 1000
    assert facts['real_group_id'] == 1000
    assert facts['effective_group_id'] == 1000

def test_collect_user_facts_keyerror(mock_getpass_getuser, mock_pwd_getpwuid, mock_os_functions, mocker):
    mocker.patch('pwd.getpwnam', side_effect=KeyError)
    collector = UserFactCollector()
    facts = collector.collect()
    
    assert facts['user_id'] == 'testuser'
    assert facts['user_uid'] == 1001
    assert facts['user_gid'] == 1001
    assert facts['user_gecos'] == 'Fallback User'
    assert facts['user_dir'] == '/home/fallbackuser'
    assert facts['user_shell'] == '/bin/sh'
    assert facts['real_user_id'] == 1000
    assert facts['effective_user_id'] == 1000
    assert facts['real_group_id'] == 1000
    assert facts['effective_group_id'] == 1000
