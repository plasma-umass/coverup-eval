# file lib/ansible/module_utils/yumdnf.py:138-139
# lines [139]
# branches []

import os
import pytest
from ansible.module_utils.yumdnf import YumDnf
from unittest.mock import patch, MagicMock

class MockYumDnf(YumDnf):
    def __init__(self, lockfile):
        self.lockfile = lockfile

    def is_lockfile_pid_valid(self):
        return True

    def run(self):
        pass  # Mock implementation of abstract method

@pytest.fixture
def mock_lockfile(tmp_path):
    lockfile = tmp_path / "lockfile"
    lockfile.touch()
    return str(lockfile)

@pytest.fixture
def mock_glob(mocker):
    return mocker.patch('glob.glob', return_value=True)

def test_is_lockfile_present_with_file(mock_lockfile):
    yum_dnf = MockYumDnf(mock_lockfile)
    assert yum_dnf._is_lockfile_present() == True

def test_is_lockfile_present_with_glob(mock_glob):
    yum_dnf = MockYumDnf("nonexistent_lockfile")
    assert yum_dnf._is_lockfile_present() == True
