# file: lib/ansible/modules/pip.py:610-621
# asked: {"lines": [610, 611, 612, 613, 614, 615, 617, 618, 619, 620], "branches": [[611, 612], [611, 613]]}
# gained: {"lines": [610, 611, 612, 613, 614, 615, 617, 618, 619, 620], "branches": [[611, 612], [611, 613]]}

import pytest
from unittest.mock import Mock
from ansible.modules.pip import Package
from ansible.module_utils.compat.version import LooseVersion

def test_is_satisfied_by_with_plain_package_and_specifier(monkeypatch):
    # Mocking the Package object
    package = Package("testpackage>=1.0.0")
    package._plain_package = True
    package._requirement.specifier = Mock()
    package._requirement.specifier.contains = Mock(return_value=True)

    assert package.is_satisfied_by("1.0.1") is True
    package._requirement.specifier.contains.assert_called_once_with("1.0.1", prereleases=True)

def test_is_satisfied_by_with_plain_package_and_no_specifier(monkeypatch):
    # Mocking the Package object
    package = Package("testpackage>=1.0.0")
    package._plain_package = True
    package._requirement.specifier = None
    package._requirement.specs = [('>=', '1.0.0')]

    def mock_contains(version, prereleases):
        raise AttributeError

    monkeypatch.setattr(package._requirement, 'specifier', Mock())
    package._requirement.specifier.contains = mock_contains

    assert package.is_satisfied_by("1.0.1") is True

def test_is_satisfied_by_with_non_plain_package():
    # Mocking the Package object
    package = Package("testpackage>=1.0.0")
    package._plain_package = False

    assert package.is_satisfied_by("1.0.1") is False
