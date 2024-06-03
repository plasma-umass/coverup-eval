# file lib/ansible/cli/doc.py:962-983
# lines [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983]
# branches ['964->966', '964->983', '970->971', '970->972', '972->973', '972->974', '974->975', '974->977']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def doc_cli():
    cli = DocCLI(args=['dummy_arg'])
    cli.plugin_list = ['plugin1', 'plugin2', 'plugin3']
    return cli

def test_get_plugin_list_filenames_success(doc_cli, mock_loader):
    mock_loader.find_plugin.side_effect = [
        '/path/to/plugin1.py',
        '/path/to/plugin2.py',
        '/path/to/plugin3.py'
    ]

    result = doc_cli._get_plugin_list_filenames(mock_loader)
    assert result == {
        'plugin1': '/path/to/plugin1.py',
        'plugin2': '/path/to/plugin2.py',
        'plugin3': '/path/to/plugin3.py'
    }

def test_get_plugin_list_filenames_non_python_file(doc_cli, mock_loader):
    mock_loader.find_plugin.side_effect = [
        '/path/to/plugin1.ps1',
        '/path/to/plugin2.py',
        '/path/to/plugin3.py'
    ]

    result = doc_cli._get_plugin_list_filenames(mock_loader)
    assert result == {
        'plugin2': '/path/to/plugin2.py',
        'plugin3': '/path/to/plugin3.py'
    }

def test_get_plugin_list_filenames_directory(doc_cli, mock_loader):
    mock_loader.find_plugin.side_effect = [
        '/path/to/plugin1.py',
        '/path/to/plugin2',
        '/path/to/plugin3.py'
    ]

    with patch('os.path.isdir', side_effect=[False, True, False]):
        result = doc_cli._get_plugin_list_filenames(mock_loader)
        assert result == {
            'plugin1': '/path/to/plugin1.py',
            'plugin3': '/path/to/plugin3.py'
        }

def test_get_plugin_list_filenames_exception(doc_cli, mock_loader):
    mock_loader.find_plugin.side_effect = Exception("Test exception")

    with patch('ansible.cli.doc.display.vvv') as mock_vvv:
        with pytest.raises(AnsibleError, match="Failed reading docs at plugin1: Test exception"):
            doc_cli._get_plugin_list_filenames(mock_loader)
        assert mock_vvv.called
