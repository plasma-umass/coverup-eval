# file: lib/ansible/modules/pip.py:628-631
# asked: {"lines": [628, 629, 630, 631], "branches": [[629, 630], [629, 631]]}
# gained: {"lines": [628, 629, 630], "branches": [[629, 630]]}

import pytest
from ansible.modules.pip import Package
from ansible.module_utils._text import to_native

def test_package_str_with_plain_package(monkeypatch):
    def mock_to_native(value):
        return value

    monkeypatch.setattr('ansible.module_utils._text.to_native', mock_to_native)

    pkg = Package("testpackage==1.0")
    assert str(pkg) == "testpackage==1.0"

def test_package_str_without_plain_package():
    pkg = Package("testpackage")
    assert str(pkg) == "testpackage"
