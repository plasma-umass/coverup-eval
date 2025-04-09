# file: lib/ansible/cli/console.py:147-158
# asked: {"lines": [], "branches": [[151, 150], [156, 155]]}
# gained: {"lines": [], "branches": [[151, 150], [156, 155]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible import context
from ansible.plugins.loader import module_loader

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['fake_arg'])

def test_list_modules_with_module_path(console_cli, monkeypatch):
    mock_module_loader = mock.MagicMock()
    monkeypatch.setattr(module_loader, 'add_directory', mock_module_loader.add_directory)
    monkeypatch.setattr(module_loader, '_get_paths', lambda: ['/fake/path1', '/fake/path2'])
    monkeypatch.setattr(context, 'CLIARGS', {'module_path': ['/fake/path1', None]})

    result = console_cli.list_modules()

    mock_module_loader.add_directory.assert_called_once_with('/fake/path1')
    assert isinstance(result, set)

def test_list_modules_without_module_path(console_cli, monkeypatch):
    mock_module_loader = mock.MagicMock()
    monkeypatch.setattr(module_loader, '_get_paths', lambda: [None, '/fake/path2'])
    monkeypatch.setattr(context, 'CLIARGS', {'module_path': None})
    monkeypatch.setattr(console_cli, '_find_modules_in_path', lambda path: {f'module_in_{path}'})

    result = console_cli.list_modules()

    assert result == {'module_in_/fake/path2'}
