# file: lib/ansible/cli/doc.py:515-517
# asked: {"lines": [517], "branches": []}
# gained: {"lines": [517], "branches": []}

import pytest
from unittest.mock import patch
import pkgutil
from ansible.cli.doc import DocCLI

def test_list_keywords():
    mock_data = b"key: value"
    
    with patch.object(pkgutil, 'get_data', return_value=mock_data) as mock_get_data:
        result = DocCLI._list_keywords()
        mock_get_data.assert_called_once_with('ansible', 'keyword_desc.yml')
        assert result == {'key': 'value'}
