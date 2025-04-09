# file lib/ansible/cli/doc.py:74-75
# lines [74, 75]
# branches []

import pytest
from ansible.cli.doc import PluginNotFound

def test_plugin_not_found_exception():
    with pytest.raises(PluginNotFound) as exc_info:
        raise PluginNotFound("Test plugin not found")

    assert str(exc_info.value) == "Test plugin not found", "PluginNotFound exception message does not match"
