# file: lib/ansible/plugins/loader.py:52-53
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader

# Mocking a PluginLoader class for testing purposes
class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass

def test_get_all_plugin_loaders(monkeypatch):
    # Mocking the globals() to include a PluginLoader instance
    mock_globals = {
        'mock_loader': MockPluginLoader(),
        'not_a_loader': 'just_a_string'
    }
    
    monkeypatch.setattr('builtins.globals', lambda: mock_globals)
    
    from ansible.plugins.loader import get_all_plugin_loaders
    
    result = get_all_plugin_loaders()
    
    assert len(result) == 1
    assert result[0][0] == 'mock_loader'
    assert isinstance(result[0][1], MockPluginLoader)
