# file: lib/ansible/plugins/action/copy.py:402-404
# asked: {"lines": [402, 403, 404], "branches": [[403, 0], [403, 404]]}
# gained: {"lines": [402, 403, 404], "branches": [[403, 0], [403, 404]]}

import os
import pytest
from ansible.plugins.action.copy import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_remove_tempfile_if_content_defined(action_module, mocker):
    content = "some content"
    content_tempfile = "tempfile.txt"

    # Create a temporary file
    with open(content_tempfile, 'w') as f:
        f.write(content)

    # Ensure the file exists before calling the method
    assert os.path.exists(content_tempfile)

    # Mock os.remove to avoid actually deleting the file
    mocker.patch('os.remove')

    # Call the method
    action_module._remove_tempfile_if_content_defined(content, content_tempfile)

    # Assert os.remove was called with the correct argument
    os.remove.assert_called_once_with(content_tempfile)

    # Clean up
    if os.path.exists(content_tempfile):
        os.remove(content_tempfile)

def test_remove_tempfile_if_content_none(action_module, mocker):
    content = None
    content_tempfile = "tempfile.txt"

    # Create a temporary file
    with open(content_tempfile, 'w') as f:
        f.write("some content")

    # Ensure the file exists before calling the method
    assert os.path.exists(content_tempfile)

    # Mock os.remove to avoid actually deleting the file
    mocker.patch('os.remove')

    # Call the method
    action_module._remove_tempfile_if_content_defined(content, content_tempfile)

    # Assert os.remove was not called
    os.remove.assert_not_called()

    # Clean up
    if os.path.exists(content_tempfile):
        os.remove(content_tempfile)
