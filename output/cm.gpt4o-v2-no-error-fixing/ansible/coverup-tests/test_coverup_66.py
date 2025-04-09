# file: lib/ansible/cli/doc.py:962-983
# asked: {"lines": [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 975], [974, 977]]}
# gained: {"lines": [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 977]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI

@pytest.fixture
def doc_cli():
    args = Mock()
    cli = DocCLI(args)
    cli.plugin_list = {'plugin1', 'plugin2', 'plugin3'}
    return cli

def test_get_plugin_list_filenames(doc_cli):
    loader = Mock()
    loader.find_plugin.side_effect = [
        '/path/to/plugin1.py',  # valid plugin
        None,                   # plugin not found
        '/path/to/plugin3.ps1', # invalid plugin (ps1 file)
        '/path/to/plugin3'      # invalid plugin (directory)
    ]

    with patch('os.path.isdir', side_effect=[False, False, True]):
        pfiles = doc_cli._get_plugin_list_filenames(loader)

    assert 'plugin1' in pfiles
    assert pfiles['plugin1'] == '/path/to/plugin1.py'
    assert 'plugin2' not in pfiles
    assert 'plugin3' not in pfiles

def test_get_plugin_list_filenames_exception(doc_cli):
    loader = Mock()
    loader.find_plugin.side_effect = Exception("Test exception")

    with patch('ansible.cli.doc.display.vvv') as mock_vvv:
        with pytest.raises(AnsibleError, match="Failed reading docs at plugin1: Test exception"):
            doc_cli._get_plugin_list_filenames(loader)
        mock_vvv.assert_called_once()
