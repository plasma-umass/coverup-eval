# file: lib/ansible/cli/doc.py:962-983
# asked: {"lines": [963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 975], [974, 977]]}
# gained: {"lines": [963, 964, 966, 968, 970, 971, 972, 973, 974, 977, 979, 980, 981, 983], "branches": [[964, 966], [964, 983], [970, 971], [970, 972], [972, 973], [972, 974], [974, 977]]}

import os
import pytest
import traceback
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.cli.doc import DocCLI

class TestDocCLI:
    
    @pytest.fixture
    def doc_cli(self):
        args = ['test']
        doc_cli = DocCLI(args)
        doc_cli.plugin_list = ['plugin1', 'plugin2', 'plugin3']
        return doc_cli

    @patch('ansible.cli.doc.display.vvv')
    def test_get_plugin_list_filenames(self, mock_display, doc_cli):
        loader = MagicMock()
        loader.find_plugin.side_effect = [
            'plugin1.py',  # valid plugin
            None,          # plugin not found
            'plugin3.ps1', # invalid plugin type
            'plugin4.py',  # valid plugin
            'plugin5'      # directory
        ]
        
        with patch('os.path.isdir', side_effect=[False, False, False, True]):
            pfiles = doc_cli._get_plugin_list_filenames(loader)
        
        assert 'plugin1' in pfiles
        assert pfiles['plugin1'] == 'plugin1.py'
        assert 'plugin2' not in pfiles
        assert 'plugin3' not in pfiles
        assert 'plugin4' not in pfiles
        assert 'plugin5' not in pfiles

    @patch('ansible.cli.doc.display.vvv')
    def test_get_plugin_list_filenames_exception(self, mock_display, doc_cli):
        loader = MagicMock()
        loader.find_plugin.side_effect = Exception('Test exception')
        
        with pytest.raises(AnsibleError, match="Failed reading docs at plugin1: Test exception"):
            doc_cli._get_plugin_list_filenames(loader)
        
        assert mock_display.called
