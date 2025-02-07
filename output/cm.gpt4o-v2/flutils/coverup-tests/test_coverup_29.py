# file: flutils/pathutils.py:461-501
# asked: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}
# gained: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_by_name(monkeypatch):
    # Mock getpwnam to return a known value
    def mock_getpwnam(name):
        if name == "validuser":
            return pwd.struct_passwd(("validuser", "x", 1001, 1001, "Valid User", "/home/validuser", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)
    user = get_os_user("validuser")
    assert user.pw_name == "validuser"
    assert user.pw_uid == 1001

def test_get_os_user_by_uid(monkeypatch):
    # Mock getpwuid to return a known value
    def mock_getpwuid(uid):
        if uid == 1001:
            return pwd.struct_passwd(("validuser", "x", 1001, 1001, "Valid User", "/home/validuser", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(pwd, "getpwuid", mock_getpwuid)
    user = get_os_user(1001)
    assert user.pw_name == "validuser"
    assert user.pw_uid == 1001

def test_get_os_user_invalid_name(monkeypatch):
    # Mock getpwnam to raise KeyError
    def mock_getpwnam(name):
        raise KeyError

    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)
    with pytest.raises(OSError, match="The given name: 'invaliduser', is not a valid \"login name\" for this operating system."):
        get_os_user("invaliduser")

def test_get_os_user_invalid_uid(monkeypatch):
    # Mock getpwuid to raise KeyError
    def mock_getpwuid(uid):
        raise KeyError

    monkeypatch.setattr(pwd, "getpwuid", mock_getpwuid)
    with pytest.raises(OSError, match="The given uid: 9999, is not a valid uid for this operating system."):
        get_os_user(9999)

def test_get_os_user_default(monkeypatch):
    # Mock getpass.getuser and pwd.getpwnam to return a known value
    def mock_getuser():
        return "defaultuser"

    def mock_getpwnam(name):
        if name == "defaultuser":
            return pwd.struct_passwd(("defaultuser", "x", 1002, 1002, "Default User", "/home/defaultuser", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(getpass, "getuser", mock_getuser)
    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)
    user = get_os_user()
    assert user.pw_name == "defaultuser"
    assert user.pw_uid == 1002
