# file: lib/ansible/plugins/loader.py:109-112
# asked: {"lines": [109, 110, 111, 112], "branches": []}
# gained: {"lines": [109, 110, 111, 112], "branches": []}

import pytest
from ansible.plugins.loader import PluginPathContext

def test_plugin_path_context_initialization():
    path = "/some/path"
    internal = True
    context = PluginPathContext(path, internal)
    
    assert context.path == path
    assert context.internal == internal
