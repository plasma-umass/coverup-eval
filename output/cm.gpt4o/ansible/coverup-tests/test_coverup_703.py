# file lib/ansible/plugins/action/validate_argument_spec.py:15-19
# lines [15, 16, 18]
# branches []

import pytest
from ansible.plugins.action import ActionBase
from ansible.plugins.action.validate_argument_spec import ActionModule

def test_action_module_transfers_files():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module.TRANSFERS_FILES is False
