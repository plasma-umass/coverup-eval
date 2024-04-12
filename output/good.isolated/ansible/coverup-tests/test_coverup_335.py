# file lib/ansible/module_utils/facts/packages.py:53-69
# lines [53, 55, 57, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69]
# branches []

import pytest
from ansible.module_utils.facts.packages import LibMgr

class TestLibMgr(LibMgr):
    LIB = "os"

    def get_package_details(self):
        pass

    def list_installed(self):
        pass

def test_libmgr_is_available(mocker):
    mocker.patch.object(TestLibMgr, '__init__', return_value=None)
    libmgr = TestLibMgr()
    assert libmgr.is_available() == True

def test_libmgr_is_not_available(mocker):
    mocker.patch.object(TestLibMgr, '__init__', return_value=None)
    mocker.patch('builtins.__import__', side_effect=ImportError)
    libmgr = TestLibMgr()
    assert libmgr.is_available() == False
