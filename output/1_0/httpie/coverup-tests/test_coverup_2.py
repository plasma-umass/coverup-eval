# file httpie/plugins/builtin.py:9-10
# lines [9, 10]
# branches []

import pytest
from httpie.plugins.builtin import BuiltinAuthPlugin

def test_builtin_auth_plugin_package_name():
    plugin = BuiltinAuthPlugin()
    assert plugin.package_name == '(builtin)'
