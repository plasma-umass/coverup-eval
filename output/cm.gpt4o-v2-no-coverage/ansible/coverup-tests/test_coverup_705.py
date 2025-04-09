# file: lib/ansible/plugins/loader.py:1020-1053
# asked: {"lines": [1020, 1040, 1050, 1051, 1053], "branches": []}
# gained: {"lines": [1020, 1040, 1050, 1051, 1053], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.loader import Jinja2Loader, PluginLoader

class TestJinja2Loader:

    @patch.object(PluginLoader, 'all')
    def test_all_method(self, mock_all):
        # Setup
        mock_all.return_value = ['plugin1', 'plugin2', 'plugin3']
        loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')

        # Execute
        result = loader.all()

        # Verify
        assert result == ['plugin3', 'plugin2', 'plugin1']
        mock_all.assert_called_once()
        assert mock_all.call_args[1]['_dedupe'] is False
