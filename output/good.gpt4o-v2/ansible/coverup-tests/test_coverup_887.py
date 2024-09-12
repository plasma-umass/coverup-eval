# file: lib/ansible/plugins/loader.py:52-53
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from ansible.plugins.loader import get_all_plugin_loaders, PluginLoader

def test_get_all_plugin_loaders(monkeypatch):
    # Setup: Create a mock PluginLoader instance and add it to a mock globals dictionary
    mock_loader = PluginLoader(class_name="mock_class", package="mock_package", config=None, subdir="mock_subdir")
    mock_globals = {'mock_loader': mock_loader}

    # Monkeypatch the globals() function to return the mock globals dictionary
    monkeypatch.setattr('builtins.globals', lambda: mock_globals)

    # Execute: Call the function to test
    result = get_all_plugin_loaders()

    # Verify: Check that the result contains the mock loader
    assert ('mock_loader', mock_loader) in result
