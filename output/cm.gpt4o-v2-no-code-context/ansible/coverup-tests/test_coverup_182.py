# file: lib/ansible/plugins/loader.py:56-66
# asked: {"lines": [56, 58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 60], [61, 62], [63, 60], [63, 64]]}
# gained: {"lines": [56, 58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 60], [61, 62], [63, 64]]}

import os
import pytest
from unittest import mock
from ansible.plugins.loader import add_all_plugin_dirs

@pytest.fixture
def mock_get_all_plugin_loaders():
    with mock.patch('ansible.plugins.loader.get_all_plugin_loaders') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_display_warning():
    with mock.patch('ansible.plugins.loader.display.warning') as mock_warning:
        yield mock_warning

def test_add_all_plugin_dirs_valid_path_with_subdir(monkeypatch, mock_get_all_plugin_loaders):
    mock_get_all_plugin_loaders.return_value = [('plugin1', mock.Mock(subdir='subdir1'))]
    mock_add_directory = mock.Mock()
    mock_get_all_plugin_loaders.return_value[0][1].add_directory = mock_add_directory

    test_path = '/tmp/test_path'
    subdir_path = os.path.join(test_path, 'subdir1')

    os.makedirs(subdir_path)

    try:
        add_all_plugin_dirs(test_path)
        mock_add_directory.assert_called_once_with(subdir_path)
    finally:
        os.rmdir(subdir_path)
        os.rmdir(test_path)

def test_add_all_plugin_dirs_valid_path_without_subdir(monkeypatch, mock_get_all_plugin_loaders):
    mock_get_all_plugin_loaders.return_value = [('plugin1', mock.Mock(subdir=None))]

    test_path = '/tmp/test_path'
    os.makedirs(test_path)

    try:
        add_all_plugin_dirs(test_path)
        mock_get_all_plugin_loaders.return_value[0][1].add_directory.assert_not_called()
    finally:
        os.rmdir(test_path)

def test_add_all_plugin_dirs_invalid_path(mock_display_warning):
    invalid_path = '/invalid/test_path'
    add_all_plugin_dirs(invalid_path)
    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path)
