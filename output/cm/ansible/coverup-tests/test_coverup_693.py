# file lib/ansible/plugins/action/copy.py:402-404
# lines [402, 403, 404]
# branches ['403->exit', '403->404']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action import copy

# Assuming the ActionModule is part of the copy module as described
class TestActionModule:
    @pytest.fixture
    def action_module(self, mocker):
        mocker.patch('ansible.plugins.action.copy.ActionBase._execute_module')
        # Mocking the required arguments for ActionModule initialization
        task = MagicMock()
        connection = MagicMock()
        play_context = MagicMock()
        loader = MagicMock()
        templar = MagicMock()
        shared_loader_obj = MagicMock()
        return copy.ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    @pytest.fixture
    def cleanup_tempfile(self):
        # Setup
        tempfiles = []

        yield tempfiles

        # Teardown
        for tempfile in tempfiles:
            if os.path.exists(tempfile):
                os.remove(tempfile)

    def test_remove_tempfile_if_content_defined(self, action_module, cleanup_tempfile, tmp_path):
        content = "dummy content"
        content_tempfile = tmp_path / "tempfile.txt"
        content_tempfile.write_text(content)
        cleanup_tempfile.append(str(content_tempfile))

        assert content_tempfile.exists()  # Ensure tempfile exists before removal

        action_module._remove_tempfile_if_content_defined(content, str(content_tempfile))

        assert not content_tempfile.exists()  # Ensure tempfile is removed

    def test_not_remove_tempfile_if_content_undefined(self, action_module, tmp_path):
        content = None
        content_tempfile = tmp_path / "tempfile.txt"
        content_tempfile.write_text("dummy content")

        assert content_tempfile.exists()  # Ensure tempfile exists before action

        action_module._remove_tempfile_if_content_defined(content, str(content_tempfile))

        assert content_tempfile.exists()  # Ensure tempfile is not removed
