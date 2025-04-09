# file lib/ansible/modules/pip.py:604-608
# lines [604, 605, 606, 607, 608]
# branches ['606->607', '606->608']

import pytest
from ansible.modules.pip import Package

class MockRequirement:
    def __init__(self, specs):
        self.specs = specs

@pytest.fixture
def package_with_version():
    package = Package('mockpackage==1.0.0')
    package._plain_package = True
    package._requirement = MockRequirement([('==', '1.0.0')])
    return package

@pytest.fixture
def package_without_version():
    package = Package('mockpackage')
    package._plain_package = True
    package._requirement = MockRequirement([])
    return package

@pytest.fixture
def non_plain_package():
    package = Package('mockpackage')
    package._plain_package = False
    package._requirement = None
    return package

def test_has_version_specifier_with_version(package_with_version):
    assert package_with_version.has_version_specifier is True

def test_has_version_specifier_without_version(package_without_version):
    assert package_without_version.has_version_specifier is False

def test_has_version_specifier_when_not_plain_package(non_plain_package):
    assert non_plain_package.has_version_specifier is False
