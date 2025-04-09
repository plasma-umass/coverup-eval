# file: flutils/pathutils.py:461-501
# asked: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}
# gained: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}

import pytest
import getpass
import pwd
from flutils.pathutils import get_os_user

def test_get_os_user_by_name(monkeypatch):
    def mock_getpwnam(name):
        if name == "existent_user":
            return pwd.struct_passwd(("existent_user", "x", 1001, 1001, "Existent User", "/home/existent_user", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)

    user = get_os_user("existent_user")
    assert user.pw_name == "existent_user"
    assert user.pw_uid == 1001

    with pytest.raises(OSError):
        get_os_user("nonexistent_user")

def test_get_os_user_by_uid(monkeypatch):
    def mock_getpwuid(uid):
        if uid == 1001:
            return pwd.struct_passwd(("existent_user", "x", 1001, 1001, "Existent User", "/home/existent_user", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(pwd, "getpwuid", mock_getpwuid)

    user = get_os_user(1001)
    assert user.pw_name == "existent_user"
    assert user.pw_uid == 1001

    with pytest.raises(OSError):
        get_os_user(9999)

def test_get_os_user_default(monkeypatch):
    def mock_getuser():
        return "default_user"

    def mock_getpwnam(name):
        if name == "default_user":
            return pwd.struct_passwd(("default_user", "x", 1002, 1002, "Default User", "/home/default_user", "/bin/bash"))
        raise KeyError

    monkeypatch.setattr(getpass, "getuser", mock_getuser)
    monkeypatch.setattr(pwd, "getpwnam", mock_getpwnam)

    user = get_os_user()
    assert user.pw_name == "default_user"
    assert user.pw_uid == 1002
