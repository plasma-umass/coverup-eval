# file flutils/pathutils.py:569-571
# lines [569, 570, 571]
# branches []

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib(tmp_path, mocker):
    # Create a temporary Path object
    temp_file = tmp_path / "test.txt"
    temp_file.touch()

    # Mock the as_posix method to return a specific string
    mocker.patch.object(Path, 'as_posix', return_value=str(temp_file))

    # Call the function with the mocked Path object
    result = normalize_path(temp_file)

    # Assert that the result is a Path object and it's the expected path
    assert isinstance(result, Path)
    assert result == temp_file

    # Cleanup is handled by pytest's tmp_path fixture
