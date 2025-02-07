# file: lib/ansible/playbook/play_context.py:318-319
# asked: {"lines": [318, 319], "branches": []}
# gained: {"lines": [318, 319], "branches": []}

import pytest
from ansible.playbook.play_context import PlayContext

def test_set_become_plugin():
    pc = PlayContext()
    plugin = "test_plugin"
    pc.set_become_plugin(plugin)
    assert pc._become_plugin == plugin
