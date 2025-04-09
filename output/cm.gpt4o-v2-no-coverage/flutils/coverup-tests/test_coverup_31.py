# file: flutils/pathutils.py:138-216
# asked: {"lines": [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213, 215, 216], "branches": [[189, 190], [189, 192], [194, 195], [194, 197], [199, 200], [199, 215], [201, 202], [201, 210], [202, 201], [202, 203], [210, 0], [210, 211], [212, 0], [212, 213], [215, 0], [215, 216]]}
# gained: {"lines": [138, 140, 141, 142, 188, 189, 192, 194, 197, 199, 200, 201, 204, 208, 215, 216], "branches": [[189, 192], [194, 197], [199, 200], [199, 215], [215, 0], [215, 216]]}

import os
import pwd
import grp
import pytest
from pathlib import Path
from unittest.mock import patch

from flutils.pathutils import chown, normalize_path, get_os_user, get_os_group

@pytest.fixture
def mock_os_functions(monkeypatch):
    def mock_chown(path, uid, gid):
        pass

    def mock_getpwnam(name):
        return pwd.struct_passwd((name, 'x', 1001, 1001, '', '/home/testuser', '/bin/bash'))

    def mock_getgrnam(name):
        return grp.struct_group((name, '*', 1001, []))

    monkeypatch.setattr(os, 'chown', mock_chown)
    monkeypatch.setattr(pwd, 'getpwnam', mock_getpwnam)
    monkeypatch.setattr(grp, 'getgrnam', mock_getgrnam)

def test_chown_file_exists(mock_os_functions, tmp_path):
    test_file = tmp_path / "testfile"
    test_file.touch()
    
    chown(test_file, user='testuser', group='testgroup')
    
    assert test_file.exists()

def test_chown_file_not_exists(mock_os_functions, tmp_path):
    test_file = tmp_path / "nonexistentfile"
    
    chown(test_file, user='testuser', group='testgroup')
    
    assert not test_file.exists()

def test_chown_with_glob(mock_os_functions, tmp_path):
    test_dir = tmp_path / "testdir"
    test_dir.mkdir()
    test_file = test_dir / "testfile"
    test_file.touch()
    
    chown(test_dir / "*", user='testuser', group='testgroup')
    
    assert test_file.exists()

def test_chown_include_parent(mock_os_functions, tmp_path):
    test_dir = tmp_path / "testdir"
    test_dir.mkdir()
    test_file = test_dir / "testfile"
    test_file.touch()
    
    chown(test_dir / "*", user='testuser', group='testgroup', include_parent=True)
    
    assert test_file.exists()
    assert test_dir.exists()

def test_chown_user_group_as_int(mock_os_functions, tmp_path):
    test_file = tmp_path / "testfile"
    test_file.touch()
    
    with patch('flutils.pathutils.get_os_user', return_value=pwd.struct_passwd(('testuser', 'x', 1001, 1001, '', '/home/testuser', '/bin/bash'))):
        with patch('flutils.pathutils.get_os_group', return_value=grp.struct_group(('testgroup', '*', 1001, []))):
            chown(test_file, user=1001, group=1001)
    
    assert test_file.exists()
