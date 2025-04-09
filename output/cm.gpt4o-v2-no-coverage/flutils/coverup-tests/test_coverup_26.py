# file: flutils/pathutils.py:417-458
# asked: {"lines": [417, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 452, 453, 454, 455, 456, 457], "branches": [[441, 442], [441, 444], [444, 445], [444, 452]]}
# gained: {"lines": [417, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 452, 453, 454, 455, 456, 457], "branches": [[441, 442], [441, 444], [444, 445], [444, 452]]}

import pytest
import grp
import pwd
from flutils.pathutils import get_os_group

def test_get_os_group_by_name(monkeypatch):
    # Mock grp.getgrnam to return a known value
    def mock_getgrnam(name):
        if name == 'mockgroup':
            return grp.struct_group(('mockgroup', '*', 1001, ['mockuser']))
        raise KeyError

    monkeypatch.setattr(grp, 'getgrnam', mock_getgrnam)

    group = get_os_group('mockgroup')
    assert group.gr_name == 'mockgroup'
    assert group.gr_gid == 1001
    assert 'mockuser' in group.gr_mem

def test_get_os_group_by_gid(monkeypatch):
    # Mock grp.getgrgid to return a known value
    def mock_getgrgid(gid):
        if gid == 1001:
            return grp.struct_group(('mockgroup', '*', 1001, ['mockuser']))
        raise KeyError

    monkeypatch.setattr(grp, 'getgrgid', mock_getgrgid)

    group = get_os_group(1001)
    assert group.gr_name == 'mockgroup'
    assert group.gr_gid == 1001
    assert 'mockuser' in group.gr_mem

def test_get_os_group_invalid_name(monkeypatch):
    # Mock grp.getgrnam to raise KeyError
    def mock_getgrnam(name):
        raise KeyError

    monkeypatch.setattr(grp, 'getgrnam', mock_getgrnam)

    with pytest.raises(OSError, match="The given name: 'invalidgroup', is not a valid \"group name\" for this operating system."):
        get_os_group('invalidgroup')

def test_get_os_group_invalid_gid(monkeypatch):
    # Mock grp.getgrgid to raise KeyError
    def mock_getgrgid(gid):
        raise KeyError

    monkeypatch.setattr(grp, 'getgrgid', mock_getgrgid)

    with pytest.raises(OSError, match="The given gid: 9999, is not a valid gid for this operating system."):
        get_os_group(9999)

def test_get_os_group_default(monkeypatch):
    # Mock get_os_user to return a known value
    def mock_get_os_user():
        return pwd.struct_passwd(('mockuser', '*', 1001, 1001, 'Mock User', '/home/mockuser', '/bin/bash'))

    # Mock grp.getgrgid to return a known value
    def mock_getgrgid(gid):
        if gid == 1001:
            return grp.struct_group(('mockgroup', '*', 1001, ['mockuser']))
        raise KeyError

    monkeypatch.setattr('flutils.pathutils.get_os_user', mock_get_os_user)
    monkeypatch.setattr(grp, 'getgrgid', mock_getgrgid)

    group = get_os_group()
    assert group.gr_name == 'mockgroup'
    assert group.gr_gid == 1001
    assert 'mockuser' in group.gr_mem
