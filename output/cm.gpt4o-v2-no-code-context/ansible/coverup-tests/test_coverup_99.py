# file: lib/ansible/cli/doc.py:962-983
# asked: {"lines": [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 975], [974, 977]]}
# gained: {"lines": [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 975], [974, 977]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError

@pytest.fixture
def doc_cli():
    return DocCLI(args=['dummy_arg'])

@pytest.fixture
def mock_loader():
    return MagicMock()

def test_get_plugin_list_filenames_success(doc_cli, mock_loader):
    doc_cli.plugin_list = ['plugin1', 'plugin2']
    mock_loader.find_plugin.side_effect = ['plugin1.py', 'plugin2.py']

    result = doc_cli._get_plugin_list_filenames(mock_loader)

    assert result == {'plugin1': 'plugin1.py', 'plugin2': 'plugin2.py'}

def test_get_plugin_list_filenames_none(doc_cli, mock_loader):
    doc_cli.plugin_list = ['plugin1']
    mock_loader.find_plugin.return_value = None

    result = doc_cli._get_plugin_list_filenames(mock_loader)

    assert result == {}

def test_get_plugin_list_filenames_ps1(doc_cli, mock_loader):
    doc_cli.plugin_list = ['plugin1']
    mock_loader.find_plugin.return_value = 'plugin1.ps1'

    result = doc_cli._get_plugin_list_filenames(mock_loader)

    assert result == {}

def test_get_plugin_list_filenames_isdir(doc_cli, mock_loader):
    doc_cli.plugin_list = ['plugin1']
    mock_loader.find_plugin.return_value = 'plugin1_dir'

    with patch('os.path.isdir', return_value=True):
        result = doc_cli._get_plugin_list_filenames(mock_loader)

    assert result == {}

def test_get_plugin_list_filenames_exception(doc_cli, mock_loader):
    doc_cli.plugin_list = ['plugin1']
    mock_loader.find_plugin.side_effect = Exception('Test exception')

    with patch('ansible.cli.doc.display.vvv') as mock_vvv, pytest.raises(AnsibleError) as excinfo:
        doc_cli._get_plugin_list_filenames(mock_loader)

    assert 'Test exception' in str(excinfo.value)
    mock_vvv.assert_called_once()
