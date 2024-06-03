# file thefuck/corrector.py:22-37
# lines [29, 31, 33, 34, 35, 36, 37]
# branches ['33->exit', '33->34', '34->33', '34->35', '36->34', '36->37']

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# Assuming the function get_rules_import_paths is imported from thefuck.corrector
from thefuck.corrector import get_rules_import_paths

@pytest.fixture
def mock_settings(mocker):
    settings = mocker.patch('thefuck.corrector.settings')
    settings.user_dir = Path('/mock/user/dir')
    return settings

def test_get_rules_import_paths(mock_settings, mocker):
    mocker.patch('thefuck.corrector.Path.is_dir', return_value=True)
    mocker.patch('thefuck.corrector.Path.glob', return_value=[Path('/mock/contrib/module')])
    
    with patch.object(sys, 'path', ['/mock/sys/path']):
        with patch('thefuck.corrector.__file__', '/mock/thefuck/corrector.py'):
            paths = list(get_rules_import_paths())
    
    assert Path('/mock/thefuck/rules') in paths
    assert mock_settings.user_dir.joinpath('rules') in paths
    assert Path('/mock/contrib/module/rules') in paths
