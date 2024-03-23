# file flutils/pathutils.py:138-216
# lines [190, 195, 202, 203, 210, 211, 212, 213, 215, 216]
# branches ['189->190', '194->195', '199->215', '201->202', '201->210', '202->201', '202->203', '210->exit', '210->211', '212->exit', '212->213', '215->exit', '215->216']

import os
import pytest
from pathlib import Path
from flutils.pathutils import chown, normalize_path
from unittest.mock import patch

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
def mock_glob(mocker):
    mock_path = mocker.Mock()
    mock_path.as_posix.return_value = '/mocked_path'
    return mocker.patch.object(Path, 'glob', return_value=iter([mock_path]))

def test_chown_with_special_cases_and_include_parent(
    tmp_path,
    mock_path_exists,
    mock_path_is_dir,
    mock_path_is_file,
    mock_os_chown,
    mock_get_os_user,
    mock_get_os_group,
    mock_glob
):
    # Create a temporary directory and file for testing
    temp_dir = tmp_path / "testdir"
    temp_dir.mkdir()
    temp_file = temp_dir / "testfile"
    temp_file.touch()

    # Set the user and group to '-1' to test the special cases
    user = '-1'
    group = '-1'

    # Call chown with a glob pattern and include_parent=True
    chown(str(temp_dir / "*"), user=user, group=group, include_parent=True)

    # Check that os.chown was called for the directory and the file
    assert mock_os_chown.call_count == 2

    # Check that os.chown was called with the correct arguments
    mock_os_chown.assert_any_call('/mocked_path', -1, -1)

    # Check that the parent directory was also processed
    parent_dir = normalize_path(str(temp_dir))
    mock_os_chown.assert_any_call(parent_dir.as_posix(), -1, -1)

    # Clean up the temporary directory and file
    temp_file.unlink()
    temp_dir.rmdir()
