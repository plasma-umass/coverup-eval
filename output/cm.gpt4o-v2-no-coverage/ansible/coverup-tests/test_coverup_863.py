# file: lib/ansible/playbook/play_context.py:318-319
# asked: {"lines": [318, 319], "branches": []}
# gained: {"lines": [318, 319], "branches": []}

import pytest
from ansible.playbook.play_context import PlayContext

def test_set_become_plugin():
    play_context = PlayContext()
    plugin = "test_plugin"
    play_context.set_become_plugin(plugin)
    assert play_context._become_plugin == plugin
