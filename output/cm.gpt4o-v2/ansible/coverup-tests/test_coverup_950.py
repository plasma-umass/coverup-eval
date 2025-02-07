# file: lib/ansible/modules/pip.py:310-312
# asked: {"lines": [310, 312], "branches": []}
# gained: {"lines": [310, 312], "branches": []}

import pytest
from ansible.modules.pip import _is_package_name

def test_is_package_name():
    # Test cases for package names
    assert _is_package_name("requests")
    assert _is_package_name("flask")
    
    # Test cases for version specifiers
    assert not _is_package_name(">=1.0")
    assert not _is_package_name("<=2.0")
    assert not _is_package_name(">3.0")
    assert not _is_package_name("<4.0")
    assert not _is_package_name("==5.0")
    assert not _is_package_name("!=6.0")
    assert not _is_package_name("~=7.0")

    # Test cases for strings with leading spaces
    assert not _is_package_name("  >=1.0")
    assert not _is_package_name("  <=2.0")
    assert not _is_package_name("  >3.0")
    assert not _is_package_name("  <4.0")
    assert not _is_package_name("  ==5.0")
    assert not _is_package_name("  !=6.0")
    assert not _is_package_name("  ~=7.0")

    # Test cases for strings with leading spaces but are package names
    assert _is_package_name("  requests")
    assert _is_package_name("  flask")
