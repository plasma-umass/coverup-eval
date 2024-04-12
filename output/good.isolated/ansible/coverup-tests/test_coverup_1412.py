# file lib/ansible/cli/doc.py:134-166
# lines [150]
# branches ['149->150', '161->163']

import os
import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_os_path_isdir(mocker):
    return mocker.patch('os.path.isdir')

@pytest.fixture
def mock_os_listdir(mocker):
    return mocker.patch('os.listdir')

def test_find_all_normal_roles_skips_non_directories(role_mixin, mock_os_path_isdir, mock_os_listdir, mock_os_path_exists, tmp_path):
    # Setup a temporary directory with a file (not a directory) to simulate a non-role path
    non_role_file = tmp_path / "not_a_directory"
    non_role_file.touch()

    # Mock os.path.isdir to return False for the non_role_file
    mock_os_path_isdir.return_value = False

    # Call the method with the temporary path
    found_roles = role_mixin._find_all_normal_roles((str(non_role_file),), name_filters=None)

    # Assert that the method continues past the non-directory and returns an empty set
    assert found_roles == set()
    mock_os_path_isdir.assert_called_once_with(str(non_role_file))

def test_find_all_normal_roles_with_name_filters(role_mixin, mock_os_path_isdir, mock_os_listdir, mock_os_path_exists, tmp_path):
    # Setup a temporary directory that simulates a role directory
    role_dir = tmp_path / "roles"
    role_dir.mkdir()
    role_subdir = role_dir / "testrole"
    role_subdir.mkdir(parents=True)

    # Create a meta directory and a dummy argspec file to simulate a role with an argument spec
    meta_dir = role_subdir / "meta"
    meta_dir.mkdir()
    argspec_file = meta_dir / role_mixin.ROLE_ARGSPEC_FILES[0]  # Use the first file from ROLE_ARGSPEC_FILES
    argspec_file.touch()

    # Mock os.path.isdir to return True for the role_dir
    mock_os_path_isdir.return_value = True

    # Mock os.listdir to return the role_subdir
    mock_os_listdir.return_value = [os.path.basename(role_subdir)]

    # Mock os.path.exists to return True for the argspec_file
    mock_os_path_exists.side_effect = lambda x: x == str(argspec_file)

    # Call the method with the temporary path and a name filter that includes the test role
    found_roles = role_mixin._find_all_normal_roles((str(role_dir),), name_filters=(os.path.basename(role_subdir),))

    # Assert that the method returns the expected role
    assert found_roles == {(os.path.basename(role_subdir), str(role_subdir))}
    mock_os_path_isdir.assert_called_once_with(str(role_dir))
    mock_os_listdir.assert_called_once_with(str(role_dir))
    mock_os_path_exists.assert_called_once_with(str(argspec_file))
