# file: httpie/plugins/base.py:1-11
# asked: {"lines": [1, 4, 8, 11], "branches": []}
# gained: {"lines": [1, 4, 8, 11], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

def test_base_plugin_initial_state():
    plugin = BasePlugin()
    assert plugin.name is None
    assert plugin.description is None
    assert plugin.package_name is None

def test_base_plugin_set_name(monkeypatch):
    plugin = BasePlugin()
    monkeypatch.setattr(plugin, 'name', 'Test Plugin')
    assert plugin.name == 'Test Plugin'

def test_base_plugin_set_description(monkeypatch):
    plugin = BasePlugin()
    monkeypatch.setattr(plugin, 'description', 'Test Description')
    assert plugin.description == 'Test Description'

def test_base_plugin_set_package_name(monkeypatch):
    plugin = BasePlugin()
    monkeypatch.setattr(plugin, 'package_name', 'test_package')
    assert plugin.package_name == 'test_package'
