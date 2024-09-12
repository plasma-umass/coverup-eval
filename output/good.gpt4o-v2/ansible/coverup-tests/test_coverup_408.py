# file: lib/ansible/plugins/action/copy.py:388-400
# asked: {"lines": [388, 390, 391, 392, 393, 394, 395, 396, 397, 399, 400], "branches": []}
# gained: {"lines": [388, 390, 391, 392, 393, 394, 395, 396, 397, 399, 400], "branches": []}

import os
import tempfile
import pytest
from unittest.mock import patch, mock_open
from ansible.plugins.action.copy import ActionModule
from ansible import constants as C
from ansible.module_utils._text import to_bytes

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_create_content_tempfile_success(action_module):
    content = "test content"
    content_bytes = to_bytes(content)

    with patch('tempfile.mkstemp', return_value=(1, '/tmp/testfile')), \
         patch('os.fdopen', mock_open()) as mock_fdopen, \
         patch('os.remove') as mock_remove:
        
        result = action_module._create_content_tempfile(content)
        
        mock_fdopen.assert_called_once_with(1, 'wb')
        mock_fdopen().write.assert_called_once_with(content_bytes)
        mock_fdopen().close.assert_called_once()
        mock_remove.assert_not_called()
        
        assert result == '/tmp/testfile'

def test_create_content_tempfile_exception(action_module):
    content = "test content"
    content_bytes = to_bytes(content)

    with patch('tempfile.mkstemp', return_value=(1, '/tmp/testfile')), \
         patch('os.fdopen', mock_open()) as mock_fdopen, \
         patch('os.remove') as mock_remove:
        
        mock_fdopen.return_value.write.side_effect = Exception("write error")
        
        with pytest.raises(Exception, match="write error"):
            action_module._create_content_tempfile(content)
        
        mock_fdopen.assert_called_once_with(1, 'wb')
        mock_fdopen.return_value.write.assert_called_once_with(content_bytes)
        mock_fdopen.return_value.close.assert_called_once()
        mock_remove.assert_called_once_with('/tmp/testfile')
