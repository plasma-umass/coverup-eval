# file lib/ansible/module_utils/facts/packages.py:19-50
# lines [25, 30, 35, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50]
# branches ['41->42', '41->50', '43->44', '43->45', '46->47', '46->49']

import pytest
from unittest.mock import MagicMock
from abc import ABCMeta, abstractmethod

# Assuming the provided code is in a file named `packages.py` within a module named `ansible.module_utils.facts`
from ansible.module_utils.facts.packages import PkgMgr

class MockPkgMgr(PkgMgr):
    def is_available(self):
        return True

    def list_installed(self):
        return ['pkg1', 'pkg2']

    def get_package_details(self, package):
        if package == 'pkg1':
            return {'name': 'pkg1', 'version': '1.0'}
        elif package == 'pkg2':
            return {'name': 'pkg2', 'version': '2.0', 'source': 'custom_source'}

@pytest.fixture
def mock_pkg_mgr():
    return MockPkgMgr()

def test_get_packages(mock_pkg_mgr):
    installed_packages = mock_pkg_mgr.get_packages()
    assert 'pkg1' in installed_packages
    assert 'pkg2' in installed_packages
    assert installed_packages['pkg1'][0]['version'] == '1.0'
    assert installed_packages['pkg1'][0]['source'] == 'mockpkgmgr'
    assert installed_packages['pkg2'][0]['version'] == '2.0'
    assert installed_packages['pkg2'][0]['source'] == 'custom_source'
