# file: lib/ansible/plugins/action/copy.py:402-404
# asked: {"lines": [402, 403, 404], "branches": [[403, 0], [403, 404]]}
# gained: {"lines": [402, 403, 404], "branches": [[403, 0], [403, 404]]}

import os
import pytest
from unittest.mock import patch
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_remove_tempfile_if_content_defined(action_module):
    content = "some content"
    content_tempfile = "tempfile.txt"

    with patch("os.remove") as mock_remove:
        action_module._remove_tempfile_if_content_defined(content, content_tempfile)
        mock_remove.assert_called_once_with(content_tempfile)

def test_remove_tempfile_if_content_not_defined(action_module):
    content = None
    content_tempfile = "tempfile.txt"

    with patch("os.remove") as mock_remove:
        action_module._remove_tempfile_if_content_defined(content, content_tempfile)
        mock_remove.assert_not_called()
