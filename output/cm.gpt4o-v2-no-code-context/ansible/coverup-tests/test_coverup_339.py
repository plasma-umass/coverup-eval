# file: lib/ansible/cli/doc.py:762-770
# asked: {"lines": [762, 763, 764, 765, 766, 767, 768, 769, 770], "branches": [[767, 768], [767, 770]]}
# gained: {"lines": [762, 763, 764, 765, 766, 767, 768, 769, 770], "branches": [[767, 768], [767, 770]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_plugin_loader():
    with patch('ansible.cli.doc.plugin_loader') as mock_loader:
        yield mock_loader

def test_get_all_plugins_of_type(mock_plugin_loader):
    # Mock the loader and its methods
    mock_loader_instance = MagicMock()
    mock_loader_instance._get_paths_with_context.return_value = [
        MagicMock(path='path1', internal=False),
        MagicMock(path='path2', internal=True)
    ]
    mock_plugin_loader.some_loader = mock_loader_instance

    # Mock the find_plugins method
    with patch.object(DocCLI, 'find_plugins', side_effect=[{'plugin1', 'plugin2'}, {'plugin3'}]) as mock_find_plugins:
        result = DocCLI.get_all_plugins_of_type('some')
        
        # Assertions to verify the correct behavior
        assert result == ['plugin1', 'plugin2', 'plugin3']
        mock_loader_instance._get_paths_with_context.assert_called_once()
        mock_find_plugins.assert_any_call('path1', False, 'some')
        mock_find_plugins.assert_any_call('path2', True, 'some')
