# file thefuck/rules/dirty_unzip.py:7-12
# lines [7, 8, 9, 10, 11, 12]
# branches []

import pytest
import zipfile
import os

from thefuck.rules.dirty_unzip import _is_bad_zip

@pytest.fixture
def create_zip_file(tmp_path):
    def _create_zip_file(file_name, files):
        zip_path = tmp_path / file_name
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                zipf.writestr(file, "This is some content")
        return zip_path
    return _create_zip_file

def test_is_bad_zip_with_multiple_files(create_zip_file):
    zip_path = create_zip_file("test.zip", ["file1.txt", "file2.txt"])
    assert _is_bad_zip(zip_path) == True

def test_is_bad_zip_with_single_file(create_zip_file):
    zip_path = create_zip_file("test.zip", ["file1.txt"])
    assert _is_bad_zip(zip_path) == False

def test_is_bad_zip_with_invalid_zip(tmp_path):
    invalid_zip_path = tmp_path / "invalid.zip"
    with open(invalid_zip_path, 'w') as f:
        f.write("This is not a zip file")
    assert _is_bad_zip(invalid_zip_path) == False
