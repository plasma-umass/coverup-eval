# file thefuck/rules/dirty_unzip.py:45-57
# lines [54, 57]
# branches []

import os
import zipfile
import pytest
from unittest import mock
from thefuck.rules.dirty_unzip import side_effect

@pytest.fixture
def mock_zip_file(tmp_path):
    zip_path = tmp_path / "test.zip"
    with zipfile.ZipFile(zip_path, 'w') as archive:
        archive.writestr("testfile.txt", "This is a test file.")
        archive.writestr("../outsidefile.txt", "This file is outside the current directory.")
    return zip_path

def test_side_effect_oserror_handling(mock_zip_file, mocker):
    old_cmd = mock.Mock()
    old_cmd.script_parts = ["unzip", str(mock_zip_file)]
    command = mock.Mock()

    # Mock os.remove to raise OSError for testing the exception handling
    def mock_remove(path):
        if path.endswith("testfile.txt"):
            raise OSError
        return

    mocker.patch("os.remove", side_effect=mock_remove)

    # Run the side_effect function
    side_effect(old_cmd, command)

    # Assert that os.remove was called with the correct file path
    os.remove.assert_any_call("testfile.txt")

    # Clean up: Ensure the file is removed if it was not already
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")
