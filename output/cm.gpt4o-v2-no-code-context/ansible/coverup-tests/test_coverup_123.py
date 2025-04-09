# file: lib/ansible/modules/pip.py:583-602
# asked: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 596, 597, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 596], [595, 599]]}
# gained: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 599]]}

import pytest
from ansible.modules.pip import Package
from pkg_resources import Requirement

def test_package_init_with_version_string():
    pkg = Package("example", "1.0.0")
    assert pkg.package_name == "example"
    assert pkg._requirement is not None
    assert pkg._plain_package is True

def test_package_init_without_version_string():
    pkg = Package("example")
    assert pkg.package_name == "example"
    assert pkg._requirement is not None
    assert pkg._plain_package is True

def test_package_init_with_non_digit_version_string():
    pkg = Package("example", ">=1.0.0")
    assert pkg.package_name == "example"
    assert pkg._requirement is not None
    assert pkg._plain_package is True

def test_package_init_with_distribute():
    pkg = Package("setuptools", "0.6c11")
    assert pkg.package_name == "setuptools"
    assert pkg._requirement is not None
    assert pkg._plain_package is True

def test_package_init_with_invalid_requirement(monkeypatch):
    def mock_parse(name_string):
        raise ValueError("Invalid requirement")
    monkeypatch.setattr(Requirement, "parse", mock_parse)
    pkg = Package("invalid_package")
    assert pkg.package_name == "invalid_package"
    assert pkg._requirement is None
    assert pkg._plain_package is False
