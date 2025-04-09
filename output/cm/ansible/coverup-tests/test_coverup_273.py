# file lib/ansible/modules/pip.py:381-393
# lines [381, 383, 384, 385, 386, 388, 390, 391, 393]
# branches ['383->384', '383->393', '384->385', '384->388', '390->383', '390->391']

import pytest
from ansible.modules.pip import _is_present
from packaging.requirements import Requirement
from packaging.version import parse as parse_version

class MockPackage:
    @staticmethod
    def canonicalize_name(name):
        return name.lower()

class MockRequirement:
    def __init__(self, name, version):
        self.package_name = name
        self.version = version

    def is_satisfied_by(self, version):
        return parse_version(version) >= parse_version(self.version)

@pytest.fixture
def mock_package(mocker):
    mocker.patch('ansible.modules.pip.Package', new=MockPackage)

def test_is_present_with_satisfied_requirement(mock_package):
    installed_pkgs = ['Foo==1.0.0', 'Bar==2.0.0']
    req = MockRequirement('foo', '1.0.0')
    assert _is_present(None, req, installed_pkgs, None) is True

def test_is_present_with_unsatisfied_requirement(mock_package):
    installed_pkgs = ['Foo==0.9.0', 'Bar==2.0.0']
    req = MockRequirement('foo', '1.0.0')
    assert _is_present(None, req, installed_pkgs, None) is False

def test_is_present_with_no_version_specified(mock_package):
    installed_pkgs = ['Foo', 'Bar==2.0.0']
    req = MockRequirement('foo', '1.0.0')
    assert _is_present(None, req, installed_pkgs, None) is False
