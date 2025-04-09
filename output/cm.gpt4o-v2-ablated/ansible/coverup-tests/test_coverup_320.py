# file: lib/ansible/cli/doc.py:74-75
# asked: {"lines": [74, 75], "branches": []}
# gained: {"lines": [74, 75], "branches": []}

import pytest

from ansible.cli.doc import PluginNotFound

def test_plugin_not_found_exception():
    with pytest.raises(PluginNotFound):
        raise PluginNotFound("Plugin not found")

    try:
        raise PluginNotFound("Plugin not found")
    except PluginNotFound as e:
        assert str(e) == "Plugin not found"
