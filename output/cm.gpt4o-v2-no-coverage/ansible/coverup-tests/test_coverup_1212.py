# file: lib/ansible/modules/pip.py:628-631
# asked: {"lines": [631], "branches": [[629, 631]]}
# gained: {"lines": [631], "branches": [[629, 631]]}

import pytest
from ansible.modules.pip import Package
from ansible.module_utils._text import to_native

def test_package_str_with_plain_package(monkeypatch):
    # Arrange
    package = Package("example", "1.0.0")
    assert package._plain_package is True  # Ensure _plain_package is True

    # Act
    result = str(package)

    # Assert
    assert result == to_native(package._requirement)

def test_package_str_without_plain_package(monkeypatch):
    # Arrange
    package = Package("example")
    monkeypatch.setattr(package, "_plain_package", False)  # Ensure _plain_package is False

    # Act
    result = str(package)

    # Assert
    assert result == package.package_name
