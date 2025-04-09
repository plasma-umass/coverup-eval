# file: lib/ansible/modules/apt_repository.py:280-289
# asked: {"lines": [280, 281, 285, 286, 287, 288, 289], "branches": []}
# gained: {"lines": [280, 281, 285, 286, 287, 288, 289], "branches": []}

import pytest
from unittest import mock

# Assuming the SourcesList class is imported from the module
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def mock_apt_pkg(monkeypatch):
    apt_pkg_mock = mock.Mock()
    monkeypatch.setattr('ansible.modules.apt_repository.apt_pkg', apt_pkg_mock)
    return apt_pkg_mock

def test_apt_cfg_file_find_file(mock_apt_pkg):
    mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
    result = SourcesList._apt_cfg_file('sources.list')
    assert result == '/etc/apt/sources.list'
    mock_apt_pkg.config.find_file.assert_called_once_with('sources.list')

def test_apt_cfg_file_find_file_attribute_error(mock_apt_pkg):
    mock_apt_pkg.config.find_file.side_effect = AttributeError
    mock_apt_pkg.Config.FindFile.return_value = '/etc/apt/sources.list'
    result = SourcesList._apt_cfg_file('sources.list')
    assert result == '/etc/apt/sources.list'
    mock_apt_pkg.Config.FindFile.assert_called_once_with('sources.list')
