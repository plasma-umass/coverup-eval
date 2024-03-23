# file flutils/pathutils.py:51-135
# lines [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 117, 122, 123, 126, 127, 128, 129, 131, 132, 133, 134, 135]
# branches ['105->106', '105->108', '108->109', '108->111', '111->112', '111->131', '113->114', '113->126', '114->115', '114->116', '116->113', '116->117', '126->exit', '126->127', '128->exit', '128->129', '131->exit', '131->132', '132->133', '132->134', '134->exit', '134->135']

import os
import pytest
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture
def temp_dir(tmp_path):
    # Create a temporary directory with a file and a subdirectory
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "testfile.txt"
    f.touch()
    return tmp_path

def test_chmod_include_parent(temp_dir, mocker):
    # Mock the normalize_path function to return a glob pattern
    mocker.patch('flutils.pathutils.normalize_path', return_value=Path(temp_dir / "sub" / "*"))

    # Mock the Path().glob method to raise NotImplementedError
    mocker.patch('pathlib.Path.glob', side_effect=NotImplementedError)

    # Set the mode for file and directory
    mode_file = 0o644
    mode_dir = 0o755

    # Change the parent directory mode to something different
    parent_dir = temp_dir / "sub"
    parent_dir.chmod(0o700)

    # Call chmod with include_parent=True to trigger the missing branch
    chmod(temp_dir / "sub" / "*", mode_file=mode_file, mode_dir=mode_dir, include_parent=True)

    # Assert that the parent directory mode has not changed because of the NotImplementedError
    parent_mode = os.stat(parent_dir).st_mode & 0o777
    assert parent_mode == 0o700, "Parent directory mode should not have changed due to NotImplementedError"

    # Cleanup is handled by the tmp_path fixture automatically
