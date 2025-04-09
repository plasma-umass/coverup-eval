# file: flutils/pathutils.py:461-501
# asked: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}
# gained: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_by_uid(monkeypatch):
    # Mock pwd.getpwuid to return a known value
    def mock_getpwuid(uid):
        if uid == 1001:
            return pwd.struct_passwd(('foo', 'x', 1001, 2001, 'Foo Bar', '/home/foo', '/usr/local/bin/bash'))
        raise KeyError
    monkeypatch.setattr(pwd, 'getpwuid', mock_getpwuid)

    # Test valid uid
    user = get_os_user(1001)
    assert user.pw_name == 'foo'
    assert user.pw_uid == 1001

    # Test invalid uid
    with pytest.raises(OSError, match="The given uid: 9999, is not a valid uid for this operating system."):
        get_os_user(9999)

def test_get_os_user_by_name(monkeypatch):
    # Mock pwd.getpwnam to return a known value
    def mock_getpwnam(name):
        if name == 'foo':
            return pwd.struct_passwd(('foo', 'x', 1001, 2001, 'Foo Bar', '/home/foo', '/usr/local/bin/bash'))
        raise KeyError
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)

    # Test valid name
    user = get_os_user('foo')
    assert user.pw_name == 'foo'
    assert user.pw_uid == 1001

    # Test invalid name
    with pytest.raises(OSError, match="The given name: 'bar', is not a valid \"login name\" for this operating system."):
        get_os_user('bar')

def test_get_os_user_default(monkeypatch):
    # Mock getpass.getuser to return a known value
    def mock_getuser():
        return 'foo'
    monkeypatch.setattr(getpass, 'getuser', mock_getuser)

    # Mock pwd.getpwnam to return a known value
    def mock_getpwnam(name):
        if name == 'foo':
            return pwd.struct_passwd(('foo', 'x', 1001, 2001, 'Foo Bar', '/home/foo', '/usr/local/bin/bash'))
        raise KeyError
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)

    # Test default user
    user = get_os_user()
    assert user.pw_name == 'foo'
    assert user.pw_uid == 1001
