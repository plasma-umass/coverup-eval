# file: lib/ansible/module_utils/facts/packages.py:14-16
# asked: {"lines": [14, 16], "branches": []}
# gained: {"lines": [14, 16], "branches": []}

import pytest
from ansible.module_utils.facts.packages import get_all_pkg_managers
from ansible.module_utils.common._utils import get_all_subclasses
from ansible.module_utils.facts.packages import PkgMgr, CLIMgr, LibMgr

class TestPkgMgr1(PkgMgr):
    def is_available(self):
        return True

    def list_installed(self):
        return []

    def get_package_details(self, package):
        return {}

class TestPkgMgr2(PkgMgr):
    def is_available(self):
        return True

    def list_installed(self):
        return []

    def get_package_details(self, package):
        return {}

def test_get_all_pkg_managers(monkeypatch):
    def mock_get_all_subclasses(cls):
        return {TestPkgMgr1, TestPkgMgr2, CLIMgr, LibMgr}

    monkeypatch.setattr('ansible.module_utils.common._utils.get_all_subclasses', mock_get_all_subclasses)

    result = get_all_pkg_managers()
    expected = {
        'testpkgmgr1': TestPkgMgr1,
        'testpkgmgr2': TestPkgMgr2
    }

    assert result == expected
