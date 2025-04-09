# file: lib/ansible/modules/pip.py:623-626
# asked: {"lines": [623, 624, 626], "branches": []}
# gained: {"lines": [623, 624, 626], "branches": []}

import pytest
from ansible.modules.pip import Package

def test_canonicalize_name():
    assert Package.canonicalize_name("Some_Package-Name") == "some-package-name"
    assert Package.canonicalize_name("another.package_name") == "another-package-name"
    assert Package.canonicalize_name("packageName") == "packagename"

def test_package_init_with_version():
    pkg = Package("Some_Package-Name", "1.0.0")
    assert pkg.package_name == "some-package-name"
    assert pkg._plain_package is True

def test_package_init_without_version():
    pkg = Package("Some_Package-Name")
    assert pkg.package_name == "some-package-name"
    assert pkg._plain_package is True

def test_package_init_invalid_name():
    pkg = Package("Invalid Package Name")
    assert pkg.package_name == "Invalid Package Name"
    assert pkg._plain_package is False
