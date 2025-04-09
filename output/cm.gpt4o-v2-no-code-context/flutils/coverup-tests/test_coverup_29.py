# file: flutils/pathutils.py:461-501
# asked: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}
# gained: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_by_name(monkeypatch):
    # Mock getpwnam to return a dummy user
    def mock_getpwnam(name):
        if name == 'testuser':
            return pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    user = get_os_user('testuser')
    assert user.pw_name == 'testuser'
    assert user.pw_uid == 1001

def test_get_os_user_by_uid(monkeypatch):
    # Mock getpwuid to return a dummy user
    def mock_getpwuid(uid):
        if uid == 1001:
            return pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)
    user = get_os_user(1001)
    assert user.pw_name == 'testuser'
    assert user.pw_uid == 1001

def test_get_os_user_current_user(monkeypatch):
    # Mock getuser and getpwnam to return a dummy user
    def mock_getuser():
        return 'currentuser'

    def mock_getpwnam(name):
        if name == 'currentuser':
            return pwd.struct_passwd(('currentuser', 'x', 1002, 1002, 'Current User', '/home/currentuser', '/bin/bash'))
        raise KeyError

    monkeypatch.setattr(getpass, 'getuser', mock_getuser)
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    user = get_os_user()
    assert user.pw_name == 'currentuser'
    assert user.pw_uid == 1002

def test_get_os_user_invalid_name(monkeypatch):
    # Mock getpwnam to raise KeyError
    def mock_getpwnam(name):
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    with pytest.raises(OSError, match="The given name: 'invaliduser', is not a valid \"login name\" for this operating system."):
        get_os_user('invaliduser')

def test_get_os_user_invalid_uid(monkeypatch):
    # Mock getpwuid to raise KeyError
    def mock_getpwuid(uid):
        raise KeyError

    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)
    with pytest.raises(OSError, match="The given uid: 9999, is not a valid uid for this operating system."):
        get_os_user(9999)
