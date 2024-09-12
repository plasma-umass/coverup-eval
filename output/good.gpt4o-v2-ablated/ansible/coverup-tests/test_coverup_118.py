# file: lib/ansible/modules/pip.py:381-393
# asked: {"lines": [381, 383, 384, 385, 386, 388, 390, 391, 393], "branches": [[383, 384], [383, 393], [384, 385], [384, 388], [390, 383], [390, 391]]}
# gained: {"lines": [381, 383, 384, 385, 386, 388, 390, 391, 393], "branches": [[383, 384], [383, 393], [384, 385], [384, 388], [390, 383], [390, 391]]}

import pytest
from unittest.mock import Mock

class Package:
    @staticmethod
    def canonicalize_name(name):
        return name.lower()

class Requirement:
    def __init__(self, package_name, version):
        self.package_name = package_name
        self.version = version

    def is_satisfied_by(self, version):
        return self.version == version

def test_is_present_with_installed_package(monkeypatch):
    from ansible.modules.pip import _is_present

    req = Requirement('testpkg', '1.0.0')
    installed_pkgs = ['testpkg==1.0.0']
    pkg_command = Mock()

    monkeypatch.setattr(Package, 'canonicalize_name', lambda name: name.lower())
    monkeypatch.setattr(Requirement, 'is_satisfied_by', lambda self, version: self.version == version)

    assert _is_present(Mock(), req, installed_pkgs, pkg_command) == True

def test_is_present_with_not_installed_package(monkeypatch):
    from ansible.modules.pip import _is_present

    req = Requirement('testpkg', '1.0.0')
    installed_pkgs = ['otherpkg==1.0.0']
    pkg_command = Mock()

    monkeypatch.setattr(Package, 'canonicalize_name', lambda name: name.lower())
    monkeypatch.setattr(Requirement, 'is_satisfied_by', lambda self, version: self.version == version)

    assert _is_present(Mock(), req, installed_pkgs, pkg_command) == False

def test_is_present_with_no_version(monkeypatch):
    from ansible.modules.pip import _is_present

    req = Requirement('testpkg', '1.0.0')
    installed_pkgs = ['testpkg']
    pkg_command = Mock()

    monkeypatch.setattr(Package, 'canonicalize_name', lambda name: name.lower())
    monkeypatch.setattr(Requirement, 'is_satisfied_by', lambda self, version: self.version == version)

    assert _is_present(Mock(), req, installed_pkgs, pkg_command) == False
