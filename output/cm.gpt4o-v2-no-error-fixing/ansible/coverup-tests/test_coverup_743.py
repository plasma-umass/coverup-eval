# file: lib/ansible/module_utils/facts/packages.py:19-50
# asked: {"lines": [25, 30, 35, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50], "branches": [[41, 42], [41, 50], [43, 44], [43, 45], [46, 47], [46, 49]]}
# gained: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 50], "branches": [[41, 42], [41, 50], [43, 44], [46, 47]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.packages import PkgMgr

class TestPkgMgr(PkgMgr):
    def is_available(self):
        return True

    def list_installed(self):
        return ['pkg1', 'pkg2']

    def get_package_details(self, package):
        if package == 'pkg1':
            return {'name': 'pkg1', 'version': '1.0'}
        elif package == 'pkg2':
            return {'name': 'pkg2', 'version': '2.0'}

@pytest.fixture
def pkg_mgr():
    return TestPkgMgr()

def test_is_available(pkg_mgr):
    assert pkg_mgr.is_available() is True

def test_list_installed(pkg_mgr):
    assert pkg_mgr.list_installed() == ['pkg1', 'pkg2']

def test_get_package_details(pkg_mgr):
    assert pkg_mgr.get_package_details('pkg1') == {'name': 'pkg1', 'version': '1.0'}
    assert pkg_mgr.get_package_details('pkg2') == {'name': 'pkg2', 'version': '2.0'}

def test_get_packages(pkg_mgr):
    packages = pkg_mgr.get_packages()
    assert 'pkg1' in packages
    assert 'pkg2' in packages
    assert packages['pkg1'][0]['name'] == 'pkg1'
    assert packages['pkg1'][0]['version'] == '1.0'
    assert packages['pkg1'][0]['source'] == 'testpkgmgr'
    assert packages['pkg2'][0]['name'] == 'pkg2'
    assert packages['pkg2'][0]['version'] == '2.0'
    assert packages['pkg2'][0]['source'] == 'testpkgmgr'
