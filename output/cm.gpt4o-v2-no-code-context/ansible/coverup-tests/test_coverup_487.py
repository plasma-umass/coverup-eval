# file: lib/ansible/modules/apt_repository.py:291-300
# asked: {"lines": [291, 292, 296, 297, 298, 299, 300], "branches": []}
# gained: {"lines": [291, 292, 296, 297, 298, 299, 300], "branches": []}

import pytest
from unittest import mock

# Assuming the SourcesList class is imported from the module
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def mock_apt_pkg(monkeypatch):
    mock_apt_pkg = mock.Mock()
    monkeypatch.setattr('ansible.modules.apt_repository.apt_pkg', mock_apt_pkg)
    return mock_apt_pkg

def test_apt_cfg_dir_with_find_dir(mock_apt_pkg):
    mock_apt_pkg.config.find_dir.return_value = '/mocked/path'
    result = SourcesList._apt_cfg_dir('mocked_dirspec')
    assert result == '/mocked/path'
    mock_apt_pkg.config.find_dir.assert_called_once_with('mocked_dirspec')

def test_apt_cfg_dir_with_find_dir_exception(mock_apt_pkg):
    mock_apt_pkg.config.find_dir.side_effect = AttributeError
    mock_apt_pkg.Config.FindDir.return_value = '/mocked/path'
    result = SourcesList._apt_cfg_dir('mocked_dirspec')
    assert result == '/mocked/path'
    mock_apt_pkg.Config.FindDir.assert_called_once_with('mocked_dirspec')
