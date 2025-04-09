# file: lib/ansible/cli/console.py:147-158
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158], "branches": [[149, 150], [149, 154], [150, 151], [150, 154], [151, 150], [151, 152], [155, 156], [155, 158], [156, 155], [156, 157]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158], "branches": [[149, 150], [149, 154], [150, 151], [150, 154], [151, 152], [155, 156], [155, 158], [156, 157]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
from ansible import context
from ansible.plugins.loader import module_loader

@pytest.fixture
def mock_context():
    with patch('ansible.context.CLIARGS', {'module_path': ['/fake/path']}):
        yield

@pytest.fixture
def mock_module_loader():
    with patch('ansible.plugins.loader.module_loader.add_directory') as mock_add_directory, \
         patch('ansible.plugins.loader.module_loader._get_paths', return_value=['/fake/path']):
        yield mock_add_directory

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_list_modules_with_module_path(mock_context, mock_module_loader, console_cli):
    modules = console_cli.list_modules()
    mock_module_loader.assert_called_once_with('/fake/path')
    assert modules == set()

def test_list_modules_without_module_path(console_cli):
    with patch('ansible.context.CLIARGS', {'module_path': None}), \
         patch('ansible.plugins.loader.module_loader._get_paths', return_value=['/fake/path']), \
         patch.object(ConsoleCLI, '_find_modules_in_path', return_value={'fake_module'}):
        modules = console_cli.list_modules()
        assert modules == {'fake_module'}
