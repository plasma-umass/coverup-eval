# file lib/ansible/module_utils/facts/packages.py:14-16
# lines [14, 16]
# branches []

import pytest
from ansible.module_utils.facts.packages import PkgMgr, get_all_pkg_managers

# Mock PkgMgr subclasses for testing
class TestPkgMgr1(PkgMgr):
    def get_package_details(self):
        pass

    def is_available(self):
        pass

    def list_installed(self):
        pass

class TestPkgMgr2(PkgMgr):
    def get_package_details(self):
        pass

    def is_available(self):
        pass

    def list_installed(self):
        pass

# Test function to improve coverage
def test_get_all_pkg_managers(mocker):
    # Mock get_all_subclasses to return our test classes along with PkgMgr
    mocker.patch(
        'ansible.module_utils.facts.packages.get_all_subclasses',
        return_value=[TestPkgMgr1, TestPkgMgr2]
    )

    # Call the function under test
    pkg_managers = get_all_pkg_managers()

    # Assert that our test classes are in the result and PkgMgr is not
    assert 'testpkgmgr1' in pkg_managers
    assert 'testpkgmgr2' in pkg_managers
    assert 'pkgmgr' not in pkg_managers  # PkgMgr should not be included
