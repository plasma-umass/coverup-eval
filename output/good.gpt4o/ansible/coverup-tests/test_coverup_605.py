# file lib/ansible/modules/apt_repository.py:218-222
# lines [218, 219, 220, 222]
# branches ['219->220', '219->222']

import os
import pytest
from unittest import mock

# Assuming the SourcesList class is part of a module named apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list(mocker):
    mock_module = mocker.Mock()
    mock_apt_pkg = mocker.patch('ansible.modules.apt_repository.apt_pkg')
    mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
    return SourcesList(mock_module)

def test_expand_path_with_slash(sources_list):
    filename = '/etc/apt/sources.list.d/custom.list'
    expanded_path = sources_list._expand_path(filename)
    assert expanded_path == filename

def test_expand_path_without_slash(sources_list, mocker):
    filename = 'custom.list'
    mock_apt_cfg_dir = mocker.patch.object(sources_list, '_apt_cfg_dir', return_value='/etc/apt/sources.list.d')
    expected_path = os.path.abspath(os.path.join('/etc/apt/sources.list.d', filename))
    expanded_path = sources_list._expand_path(filename)
    assert expanded_path == expected_path
    mock_apt_cfg_dir.assert_called_once_with('Dir::Etc::sourceparts')
