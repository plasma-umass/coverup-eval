# file: httpie/plugins/builtin.py:9-10
# asked: {"lines": [9, 10], "branches": []}
# gained: {"lines": [9, 10], "branches": []}

import pytest
from httpie.plugins.builtin import BuiltinAuthPlugin

def test_builtin_auth_plugin_package_name():
    assert BuiltinAuthPlugin.package_name == '(builtin)'
