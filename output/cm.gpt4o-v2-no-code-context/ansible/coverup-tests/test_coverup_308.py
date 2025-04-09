# file: lib/ansible/module_utils/facts/packages.py:53-69
# asked: {"lines": [53, 55, 57, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69], "branches": []}
# gained: {"lines": [53, 55, 57, 62], "branches": []}

import pytest
from ansible.module_utils.facts.packages import PkgMgr

class TestLibMgr(PkgMgr):
    LIB = 'math'  # Use a standard library module for testing

    def __init__(self):
        self._lib = None
        super(TestLibMgr, self).__init__()

    def get_package_details(self, package_name):
        pass

    def list_installed(self):
        pass

    def is_available(self):
        found = False
        try:
            self._lib = __import__(self.LIB)
            found = True
        except ImportError:
            pass
        return found

def test_libmgr_init():
    libmgr = TestLibMgr()
    assert libmgr._lib is None

def test_libmgr_is_available_success():
    libmgr = TestLibMgr()
    assert libmgr.is_available() is True
    assert libmgr._lib is not None

def test_libmgr_is_available_failure(monkeypatch):
    class TestLibMgrFailure(PkgMgr):
        LIB = 'non_existent_module'

        def __init__(self):
            self._lib = None
            super(TestLibMgrFailure, self).__init__()

        def get_package_details(self, package_name):
            pass

        def list_installed(self):
            pass

        def is_available(self):
            found = False
            try:
                self._lib = __import__(self.LIB)
                found = True
            except ImportError:
                pass
            return found

    libmgr = TestLibMgrFailure()
    assert libmgr.is_available() is False
    assert libmgr._lib is None
