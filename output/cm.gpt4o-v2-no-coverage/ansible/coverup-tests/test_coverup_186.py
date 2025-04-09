# file: lib/ansible/modules/pip.py:583-602
# asked: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 596, 597, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 596], [595, 599]]}
# gained: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 599]]}

import pytest
from pkg_resources import Requirement
from ansible.modules.pip import Package

@pytest.fixture
def package():
    return Package("example", "1.0")

def test_package_initialization_with_version(package):
    assert package.package_name == "example"
    assert package._requirement is not None
    assert package._plain_package is True

def test_package_initialization_without_version():
    package = Package("example")
    assert package.package_name == "example"
    assert package._requirement is not None
    assert package._plain_package is True

def test_package_initialization_with_non_digit_version():
    package = Package("example", ">=1.0")
    assert package.package_name == "example"
    assert package._requirement is not None
    assert package._plain_package is True

def test_package_initialization_with_distribute():
    package = Package("setuptools", "0.7")
    assert package.package_name == "setuptools"
    assert package._requirement.project_name == "setuptools"
    assert package._plain_package is True

def test_package_initialization_with_invalid_requirement():
    package = Package("invalid_package_name", "invalid_version")
    assert package.package_name == "invalid_package_name"
    assert package._requirement is None
    assert package._plain_package is False

def test_canonicalize_name():
    assert Package.canonicalize_name("Example-Package") == "example-package"
