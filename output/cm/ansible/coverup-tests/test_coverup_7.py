# file lib/ansible/plugins/action/copy.py:55-201
# lines [55, 86, 88, 109, 110, 111, 112, 114, 116, 117, 119, 122, 125, 127, 128, 129, 130, 131, 133, 134, 135, 138, 141, 142, 143, 144, 145, 150, 151, 153, 156, 159, 160, 161, 164, 167, 171, 172, 173, 175, 179, 180, 181, 182, 183, 184, 187, 188, 189, 190, 192, 193, 194, 196, 197, 199, 201]
# branches ['109->exit', '109->110', '110->111', '110->127', '114->116', '114->125', '117->119', '117->122', '127->109', '127->128', '133->134', '133->167', '134->135', '134->164', '135->138', '135->141', '143->144', '143->153', '145->150', '145->151', '153->156', '153->159', '172->173', '172->175', '179->180', '179->181', '181->182', '181->183', '183->184', '183->187', '187->188', '187->189', '189->190', '189->192', '192->193', '192->196']

import os
import pytest
from unittest.mock import MagicMock

# Assuming the code above is in a file named `copy.py` in the `ansible.plugins.action` package
from ansible.plugins.action.copy import _walk_dirs

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create a directory structure for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    sub_dir = test_dir / "sub_dir"
    sub_dir.mkdir()
    file_path = sub_dir / "test_file.txt"
    file_path.write_text("This is a test file.")
    symlink_path = test_dir / "symlink"
    symlink_path.symlink_to(sub_dir)
    circular_symlink_path = sub_dir / "circular_symlink"
    circular_symlink_path.symlink_to(sub_dir)

    # Setup cleanup and provide paths for the test
    yield test_dir, sub_dir, file_path, symlink_path, circular_symlink_path
    # No explicit cleanup needed as tmp_path is a pytest fixture that cleans up after itself

def test_walk_dirs(mocker, setup_test_environment):
    test_dir, sub_dir, file_path, symlink_path, circular_symlink_path = setup_test_environment

    # Mock os.stat to simulate circular symlink
    original_os_stat = os.stat
    def mock_os_stat(path):
        if path == str(circular_symlink_path):
            raise FileNotFoundError
        return original_os_stat(path)

    mocker.patch('os.stat', side_effect=mock_os_stat)
    result = _walk_dirs(str(test_dir), local_follow=True)

    # Verify that the circular symlink was detected and added as a symlink
    assert (os.readlink(str(circular_symlink_path)), str(circular_symlink_path.relative_to(test_dir.parent))) in result['symlinks']

    # Now test without following symlinks
    result = _walk_dirs(str(test_dir), local_follow=False)

    # Verify that the symlink was added to the result
    assert (os.readlink(str(symlink_path)), str(symlink_path.relative_to(test_dir.parent))) in result['symlinks']

    # Verify that the file was added to the result
    assert (str(file_path), str(file_path.relative_to(test_dir.parent))) in result['files']

    # Verify that the directory was added to the result
    assert (str(sub_dir), str(sub_dir.relative_to(test_dir.parent))) in result['directories']
