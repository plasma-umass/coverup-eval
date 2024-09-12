# file: lib/ansible/modules/pip.py:623-626
# asked: {"lines": [623, 624, 626], "branches": []}
# gained: {"lines": [623, 624, 626], "branches": []}

import pytest
from ansible.modules.pip import Package

def test_canonicalize_name():
    # Test that the canonicalize_name method correctly transforms the package name
    assert Package.canonicalize_name("Some_Package-Name") == "some-package-name"
    assert Package.canonicalize_name("another.package_name") == "another-package-name"
    assert Package.canonicalize_name("packageName") == "packagename"

@pytest.fixture
def package():
    return Package("Some_Package-Name")

def test_package_initialization(package):
    # Test that the package is initialized correctly
    assert package.package_name == "some-package-name"

def test_package_canonicalize_name(package):
    # Test that the canonicalize_name method is used during initialization
    assert package.package_name == Package.canonicalize_name("Some_Package-Name")
