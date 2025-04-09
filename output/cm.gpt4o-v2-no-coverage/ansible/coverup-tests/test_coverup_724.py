# file: lib/ansible/cli/doc.py:432-437
# asked: {"lines": [432, 433, 435, 437], "branches": []}
# gained: {"lines": [432, 433, 435, 437], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI
from ansible.cli import CLI
from ansible.utils.display import Display

class MockOptions:
    def __init__(self, verbosity):
        self.verbosity = verbosity

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display', autospec=True) as mock_display:
        yield mock_display

@pytest.fixture
def doc_cli_instance():
    args = ['arg1', 'arg2']
    return DocCLI(args)

def test_post_process_args(doc_cli_instance, mock_display):
    options = MockOptions(verbosity=3)
    mock_super = MagicMock(return_value=options)
    
    with patch.object(CLI, 'post_process_args', mock_super):
        result = doc_cli_instance.post_process_args(options)
    
    mock_super.assert_called_once_with(options)
    assert result == options
    assert mock_display.verbosity == options.verbosity
