# file: httpie/plugins/manager.py:21-23
# asked: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}
# gained: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class SamplePlugin(BasePlugin):
    name = 'Sample'
    description = 'A sample plugin'
    package_name = 'sample_package'

def test_register_plugin():
    manager = PluginManager()
    manager.register(SamplePlugin)
    assert SamplePlugin in manager

def test_register_multiple_plugins():
    class AnotherPlugin(BasePlugin):
        name = 'Another'
        description = 'Another sample plugin'
        package_name = 'another_package'

    manager = PluginManager()
    manager.register(SamplePlugin, AnotherPlugin)
    assert SamplePlugin in manager
    assert AnotherPlugin in manager
