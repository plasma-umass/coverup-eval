# file flutils/pathutils.py:461-501
# lines [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500]
# branches ['485->486', '485->493', '493->494', '493->495']

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_by_name(mocker):
    # Mocking pwd.getpwnam to return a fake user
    fake_user = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    mocker.patch('pwd.getpwnam', return_value=fake_user)
    
    user = get_os_user('testuser')
    assert user.pw_name == 'testuser'
    assert user.pw_uid == 1001
    assert user.pw_gid == 1001
    assert user.pw_gecos == 'Test User'
    assert user.pw_dir == '/home/testuser'
    assert user.pw_shell == '/bin/bash'

def test_get_os_user_by_uid(mocker):
    # Mocking pwd.getpwuid to return a fake user
    fake_user = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    mocker.patch('pwd.getpwuid', return_value=fake_user)
    
    user = get_os_user(1001)
    assert user.pw_name == 'testuser'
    assert user.pw_uid == 1001
    assert user.pw_gid == 1001
    assert user.pw_gecos == 'Test User'
    assert user.pw_dir == '/home/testuser'
    assert user.pw_shell == '/bin/bash'

def test_get_os_user_current_user(mocker):
    # Mocking getpass.getuser and pwd.getpwnam to return a fake current user
    mocker.patch('getpass.getuser', return_value='currentuser')
    fake_user = pwd.struct_passwd(('currentuser', 'x', 1002, 1002, 'Current User', '/home/currentuser', '/bin/bash'))
    mocker.patch('pwd.getpwnam', return_value=fake_user)
    
    user = get_os_user()
    assert user.pw_name == 'currentuser'
    assert user.pw_uid == 1002
    assert user.pw_gid == 1002
    assert user.pw_gecos == 'Current User'
    assert user.pw_dir == '/home/currentuser'
    assert user.pw_shell == '/bin/bash'

def test_get_os_user_invalid_name(mocker):
    # Mocking pwd.getpwnam to raise KeyError
    mocker.patch('pwd.getpwnam', side_effect=KeyError)
    
    with pytest.raises(OSError, match=r'The given name: .* is not a valid "login name" for this operating system.'):
        get_os_user('invaliduser')

def test_get_os_user_invalid_uid(mocker):
    # Mocking pwd.getpwuid to raise KeyError
    mocker.patch('pwd.getpwuid', side_effect=KeyError)
    
    with pytest.raises(OSError, match=r'The given uid: .* is not a valid uid for this operating system.'):
        get_os_user(9999)
