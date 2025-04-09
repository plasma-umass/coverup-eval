# file: lib/ansible/modules/pip.py:623-626
# asked: {"lines": [623, 624, 626], "branches": []}
# gained: {"lines": [623, 624, 626], "branches": []}

import pytest
from ansible.modules.pip import Package

def test_canonicalize_name():
    # Test with underscores
    assert Package.canonicalize_name("some_package") == "some-package"
    
    # Test with dots
    assert Package.canonicalize_name("some.package") == "some-package"
    
    # Test with mixed characters
    assert Package.canonicalize_name("some-package_name") == "some-package-name"
    
    # Test with uppercase characters
    assert Package.canonicalize_name("Some_Package") == "some-package"
