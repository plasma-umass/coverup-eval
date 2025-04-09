# file: flutils/pathutils.py:461-501
# asked: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}
# gained: {"lines": [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500], "branches": [[485, 486], [485, 493], [493, 494], [493, 495]]}

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_by_name(monkeypatch):
    # Mocking pwd.getpwnam to return a known struct_passwd
    mock_pwd = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    monkeypatch.setattr(pwd, 'getpwnam', lambda name: mock_pwd)
    
    result = get_os_user('testuser')
    assert result == mock_pwd

def test_get_os_user_by_uid(monkeypatch):
    # Mocking pwd.getpwuid to return a known struct_passwd
    mock_pwd = pwd.struct_passwd(('testuser', 'x', 1001, 1001, 'Test User', '/home/testuser', '/bin/bash'))
    monkeypatch.setattr(pwd, 'getpwuid', lambda uid: mock_pwd)
    
    result = get_os_user(1001)
    assert result == mock_pwd

def test_get_os_user_by_name_not_found(monkeypatch):
    # Mocking pwd.getpwnam to raise KeyError
    monkeypatch.setattr(pwd, 'getpwnam', lambda name: (_ for _ in ()).throw(KeyError))
    
    with pytest.raises(OSError, match="The given name: 'nonexistent', is not a valid \"login name\" for this operating system."):
        get_os_user('nonexistent')

def test_get_os_user_by_uid_not_found(monkeypatch):
    # Mocking pwd.getpwuid to raise KeyError
    monkeypatch.setattr(pwd, 'getpwuid', lambda uid: (_ for _ in ()).throw(KeyError))
    
    with pytest.raises(OSError, match="The given uid: 9999, is not a valid uid for this operating system."):
        get_os_user(9999)

def test_get_os_user_default(monkeypatch):
    # Mocking getpass.getuser and pwd.getpwnam to return a known struct_passwd
    mock_pwd = pwd.struct_passwd(('defaultuser', 'x', 1001, 1001, 'Default User', '/home/defaultuser', '/bin/bash'))
    monkeypatch.setattr(getpass, 'getuser', lambda: 'defaultuser')
    monkeypatch.setattr(pwd, 'getpwnam', lambda name: mock_pwd)
    
    result = get_os_user()
    assert result == mock_pwd
