# file httpie/cli/dicts.py:57-58
# lines [57, 58]
# branches []

import pytest
from httpie.cli.dicts import RequestFilesDict
from pathlib import Path

def test_request_files_dict_initialization_and_usage(tmpdir, mocker):
    # Setup: Create a temporary file to use as a file parameter
    tmp_file = tmpdir.join("upload.txt")
    tmp_file.write("content")

    # Mock the is_file method of Path to return True, simulating a file check
    mocker.patch.object(Path, 'is_file', return_value=True)

    # Initialize the RequestFilesDict with a file parameter
    files_dict = RequestFilesDict()
    files_dict['file'] = str(tmp_file)

    # Assertions to ensure the file was added correctly
    assert 'file' in files_dict
    assert files_dict['file'] == str(tmp_file)

    # Cleanup is handled by pytest's tmpdir fixture automatically
