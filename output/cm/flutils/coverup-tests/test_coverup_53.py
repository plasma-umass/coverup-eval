# file flutils/pathutils.py:138-216
# lines [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213, 215, 216]
# branches ['189->190', '189->192', '194->195', '194->197', '199->200', '199->215', '201->202', '201->210', '202->201', '202->203', '210->exit', '210->211', '212->exit', '212->213', '215->exit', '215->216']

import os
import pytest
from pathlib import Path
from flutils.pathutils import chown, normalize_path, get_os_user, get_os_group
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_path_exists(mocker):
    return mocker.patch.object(Path, 'exists', return_value=True)

@pytest.fixture
def mock_path_is_dir(mocker):
    return mocker.patch.object(Path, 'is_dir', return_value=True)

@pytest.fixture
def mock_path_is_file(mocker):
    return mocker.patch.object(Path, 'is_file', return_value=True)

@pytest.fixture
def mock_os_chown(mocker):
    return mocker.patch('os.chown')

@pytest.fixture
def mock_get_os_user(mocker):
    mock_user = mocker.Mock()
    mock_user.pw_uid = 1000
    return mocker.patch('flutils.pathutils.get_os_user', return_value=mock_user)

@pytest.fixture
def mock_get_os_group(mocker):
    mock_group = mocker.Mock()
    mock_group.gr_gid = 1000
    return mocker.patch('flutils.pathutils.get_os_group', return_value=mock_group)

@pytest.fixture
def mock_path_glob(mocker):
    mock_glob = MagicMock()
    mock_glob.side_effect = NotImplementedError
    return mocker.patch.object(Path, 'glob', mock_glob)

def test_chown_with_glob_pattern_include_parent(
    mock_path_exists,
    mock_path_is_dir,
    mock_path_is_file,
    mock_os_chown,
    mock_get_os_user,
    mock_get_os_group,
    mock_path_glob
):
    # Setup a temporary directory and file
    chown('/tmp/*', user='nobody', group='nogroup', include_parent=True)

    # Check that get_os_user and get_os_group were called with the correct arguments
    mock_get_os_user.assert_called_with('nobody')
    mock_get_os_group.assert_called_with('nogroup')

    # Check that Path.glob was called with the correct pattern
    mock_path_glob.assert_called_with('/tmp/*')

    # Check that os.chown was not called since the glob pattern raised NotImplementedError
    mock_os_chown.assert_not_called()
