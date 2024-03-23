# file lib/ansible/plugins/action/copy.py:388-400
# lines [388, 390, 391, 392, 393, 394, 395, 396, 397, 399, 400]
# branches []

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.copy import ActionModule
from ansible.constants import DEFAULT_LOCAL_TMP
from ansible.module_utils._text import to_bytes

# Mock the constants to use a test directory for DEFAULT_LOCAL_TMP
@pytest.fixture
def mock_ansible_constants(mocker, tmp_path):
    mocker.patch('ansible.constants.DEFAULT_LOCAL_TMP', str(tmp_path))

# Mock ActionModule constructor arguments
@pytest.fixture
def mock_action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)
    return ActionModule(task={}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Test function to cover _create_content_tempfile method
def test_create_content_tempfile_success(mock_ansible_constants, mock_action_module):
    action_module = mock_action_module
    content = "Test content"
    content_tempfile = action_module._create_content_tempfile(content)
    try:
        # Verify the file was created
        assert os.path.exists(content_tempfile)
        # Verify the content of the file
        with open(content_tempfile, 'rb') as f:
            file_content = f.read()
        assert file_content == to_bytes(content)
    finally:
        # Clean up the created tempfile
        os.remove(content_tempfile)

# Test function to cover the exception branch in _create_content_tempfile method
def test_create_content_tempfile_exception(mock_ansible_constants, mock_action_module, mocker):
    mocker.patch('os.fdopen', side_effect=Exception("Mocked exception"))
    action_module = mock_action_module
    content = "Test content"
    with pytest.raises(Exception) as exc_info:
        action_module._create_content_tempfile(content)
    assert "Mocked exception" in str(exc_info.value)
    # No need to clean up as the file should not have been created due to the exception
