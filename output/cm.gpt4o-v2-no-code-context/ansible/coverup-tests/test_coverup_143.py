# file: lib/ansible/cli/console.py:147-158
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158], "branches": [[149, 150], [149, 154], [150, 151], [150, 154], [151, 150], [151, 152], [155, 156], [155, 158], [156, 155], [156, 157]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158], "branches": [[149, 150], [149, 154], [150, 151], [150, 154], [151, 152], [155, 156], [155, 158], [156, 157]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible import context
from ansible.plugins.loader import module_loader

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['fake_arg'])

def test_list_modules_with_module_path(console_cli, monkeypatch):
    # Mocking context.CLIARGS and module_loader
    mock_module_path = ['/fake/path']
    monkeypatch.setattr(context, 'CLIARGS', {'module_path': mock_module_path})
    mock_add_directory = mock.Mock()
    monkeypatch.setattr(module_loader, 'add_directory', mock_add_directory)
    mock_get_paths = mock.Mock(return_value=['/fake/path'])
    monkeypatch.setattr(module_loader, '_get_paths', mock_get_paths)
    mock_find_modules_in_path = mock.Mock(return_value={'module1', 'module2'})
    monkeypatch.setattr(console_cli, '_find_modules_in_path', mock_find_modules_in_path)

    modules = console_cli.list_modules()

    # Assertions
    mock_add_directory.assert_called_once_with('/fake/path')
    mock_get_paths.assert_called_once()
    mock_find_modules_in_path.assert_called_once_with('/fake/path')
    assert modules == {'module1', 'module2'}

def test_list_modules_without_module_path(console_cli, monkeypatch):
    # Mocking context.CLIARGS and module_loader
    monkeypatch.setattr(context, 'CLIARGS', {'module_path': None})
    mock_add_directory = mock.Mock()
    monkeypatch.setattr(module_loader, 'add_directory', mock_add_directory)
    mock_get_paths = mock.Mock(return_value=['/fake/path'])
    monkeypatch.setattr(module_loader, '_get_paths', mock_get_paths)
    mock_find_modules_in_path = mock.Mock(return_value={'module1', 'module2'})
    monkeypatch.setattr(console_cli, '_find_modules_in_path', mock_find_modules_in_path)

    modules = console_cli.list_modules()

    # Assertions
    mock_add_directory.assert_not_called()
    mock_get_paths.assert_called_once()
    mock_find_modules_in_path.assert_called_once_with('/fake/path')
    assert modules == {'module1', 'module2'}
