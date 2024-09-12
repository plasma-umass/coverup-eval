# file: lib/ansible/plugins/loader.py:1020-1053
# asked: {"lines": [1020, 1040, 1050, 1051, 1053], "branches": []}
# gained: {"lines": [1020, 1040, 1050, 1051, 1053], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import Jinja2Loader, PluginLoader

@pytest.fixture
def mock_plugin_loader():
    with patch('ansible.plugins.loader.PluginLoader.all', return_value=['plugin1', 'plugin2', 'plugin3']) as mock_all:
        yield mock_all

def test_jinja2loader_all(mock_plugin_loader):
    loader = Jinja2Loader(class_name='jinja2', package='ansible.plugins', config=None, subdir='jinja2')
    
    result = loader.all()
    
    # Ensure the super().all() method was called with the correct parameters
    mock_plugin_loader.assert_called_once_with(_dedupe=False)
    
    # Ensure the result is reversed
    assert result == ['plugin3', 'plugin2', 'plugin1']
