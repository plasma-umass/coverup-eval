# file: lib/ansible/modules/pip.py:628-631
# asked: {"lines": [628, 629, 630, 631], "branches": [[629, 630], [629, 631]]}
# gained: {"lines": [628, 629, 630, 631], "branches": [[629, 630], [629, 631]]}

import pytest
from ansible.modules.pip import Package
from ansible.module_utils._text import to_native

def test_package_str_with_plain_package(monkeypatch):
    # Arrange
    package_name = "example-package"
    version_string = "1.0.0"
    package = Package(package_name, version_string)
    
    # Act
    result = str(package)
    
    # Assert
    assert result == to_native(package._requirement)
    
def test_package_str_without_plain_package(monkeypatch):
    # Arrange
    package_name = "example-package"
    package = Package(package_name)
    package._plain_package = False  # Ensure _plain_package is False
    
    # Act
    result = str(package)
    
    # Assert
    assert result == package.package_name
