# file: lib/ansible/modules/pip.py:310-312
# asked: {"lines": [310, 312], "branches": []}
# gained: {"lines": [310, 312], "branches": []}

import pytest

def test_is_package_name_with_package_name():
    from ansible.modules.pip import _is_package_name
    assert _is_package_name('requests') == True

def test_is_package_name_with_version_specifier():
    from ansible.modules.pip import _is_package_name
    assert _is_package_name('>=2.0') == False

def test_is_package_name_with_leading_whitespace():
    from ansible.modules.pip import _is_package_name
    assert _is_package_name('  requests') == True

def test_is_package_name_with_leading_whitespace_and_version_specifier():
    from ansible.modules.pip import _is_package_name
    assert _is_package_name('  >=2.0') == False
