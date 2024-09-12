# file: httpie/plugins/base.py:1-11
# asked: {"lines": [1, 4, 8, 11], "branches": []}
# gained: {"lines": [1, 4, 8, 11], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

def test_base_plugin_initialization():
    plugin = BasePlugin()
    assert plugin.name is None
    assert plugin.description is None
    assert plugin.package_name is None
