# file: lib/ansible/modules/pip.py:381-393
# asked: {"lines": [381, 383, 384, 385, 386, 388, 390, 391, 393], "branches": [[383, 384], [383, 393], [384, 385], [384, 388], [390, 383], [390, 391]]}
# gained: {"lines": [381, 383, 384, 385, 386, 388, 390, 391, 393], "branches": [[383, 384], [383, 393], [384, 385], [384, 388], [390, 383], [390, 391]]}

import pytest
from unittest.mock import Mock

# Assuming the Package class and _is_present function are defined in the module `ansible.modules.pip`
from ansible.modules.pip import _is_present, Package

class MockRequirement:
    def __init__(self, package_name, version):
        self.package_name = package_name
        self.version = version

    def is_satisfied_by(self, version):
        return self.version == version

@pytest.fixture
def mock_package_canonicalize_name(monkeypatch):
    def mock_canonicalize_name(name):
        return name.lower()
    monkeypatch.setattr(Package, 'canonicalize_name', mock_canonicalize_name)

def test_is_present_with_equal_sign(mock_package_canonicalize_name):
    module = Mock()
    req = MockRequirement('testpkg', '1.0.0')
    installed_pkgs = ['testpkg==1.0.0']
    pkg_command = Mock()

    result = _is_present(module, req, installed_pkgs, pkg_command)
    assert result is True

def test_is_present_without_equal_sign(mock_package_canonicalize_name):
    module = Mock()
    req = MockRequirement('testpkg', '1.0.0')
    installed_pkgs = ['testpkg']
    pkg_command = Mock()

    result = _is_present(module, req, installed_pkgs, pkg_command)
    assert result is False

def test_is_present_with_unsatisfied_version(mock_package_canonicalize_name):
    module = Mock()
    req = MockRequirement('testpkg', '1.0.0')
    installed_pkgs = ['testpkg==2.0.0']
    pkg_command = Mock()

    result = _is_present(module, req, installed_pkgs, pkg_command)
    assert result is False

def test_is_present_with_multiple_packages(mock_package_canonicalize_name):
    module = Mock()
    req = MockRequirement('testpkg', '1.0.0')
    installed_pkgs = ['otherpkg==1.0.0', 'testpkg==1.0.0']
    pkg_command = Mock()

    result = _is_present(module, req, installed_pkgs, pkg_command)
    assert result is True
