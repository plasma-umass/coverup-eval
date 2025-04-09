# file: lib/ansible/modules/pip.py:310-312
# asked: {"lines": [310, 312], "branches": []}
# gained: {"lines": [310, 312], "branches": []}

import pytest
from ansible.modules.pip import _is_package_name

def test_is_package_name():
    # Test cases for package names
    assert _is_package_name("package") == True
    assert _is_package_name(" another_package") == True
    assert _is_package_name(">=1.0") == False
    assert _is_package_name("<=1.0") == False
    assert _is_package_name(">1.0") == False
    assert _is_package_name("==1.0") == False
    assert _is_package_name("!=1.0") == False
    assert _is_package_name("~=1.0") == False
