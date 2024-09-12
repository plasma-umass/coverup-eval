# file: lib/ansible/modules/pip.py:583-602
# asked: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 596, 597, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 596], [595, 599]]}
# gained: {"lines": [583, 584, 585, 586, 588, 589, 590, 591, 592, 593, 595, 596, 597, 599, 600, 601, 602], "branches": [[588, 589], [588, 592], [595, 596], [595, 599]]}

import pytest
from pkg_resources import Requirement
from ansible.modules.pip import Package

@pytest.fixture
def package():
    return Package

def test_package_init_with_version_string(package):
    pkg = package("example", "1.0")
    assert pkg._plain_package is True
    assert pkg.package_name == "example"
    assert pkg._requirement is not None
    assert pkg._requirement.project_name == "example"

def test_package_init_with_distribute(package, monkeypatch):
    def mock_parse(req):
        class MockRequirement:
            project_name = "distribute"
        return MockRequirement()
    
    monkeypatch.setattr(Requirement, "parse", mock_parse)
    pkg = package("setuptools", "1.0")
    assert pkg._plain_package is True
    assert pkg.package_name == "setuptools"
    assert pkg._requirement.project_name == "setuptools"

def test_package_init_without_version_string(package):
    pkg = package("example")
    assert pkg._plain_package is True
    assert pkg.package_name == "example"
    assert pkg._requirement is not None
    assert pkg._requirement.project_name == "example"

def test_package_init_with_invalid_requirement(package, monkeypatch):
    def mock_parse(req):
        raise ValueError("Invalid requirement")
    
    monkeypatch.setattr(Requirement, "parse", mock_parse)
    pkg = package("invalid_package")
    assert pkg._plain_package is False
    assert pkg.package_name == "invalid_package"
    assert pkg._requirement is None
