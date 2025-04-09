# file thefuck/rules/dirty_unzip.py:7-12
# lines [7, 8, 9, 10, 11, 12]
# branches []

import os
import pytest
import zipfile
from thefuck.rules.dirty_unzip import _is_bad_zip

@pytest.fixture
def single_file_zip(tmp_path):
    zip_path = tmp_path / "single_file.zip"
    with zipfile.ZipFile(zip_path, 'w') as archive:
        archive.writestr('single_file.txt', 'This is a single file inside a zip.')
    return zip_path

@pytest.fixture
def multi_file_zip(tmp_path):
    zip_path = tmp_path / "multi_file.zip"
    with zipfile.ZipFile(zip_path, 'w') as archive:
        archive.writestr('file1.txt', 'This is the first file inside a zip.')
        archive.writestr('file2.txt', 'This is the second file inside a zip.')
    return zip_path

@pytest.fixture
def bad_zip(tmp_path):
    bad_zip_path = tmp_path / "bad.zip"
    with open(bad_zip_path, 'w') as bad_zip_file:
        bad_zip_file.write("This is not a valid zip file.")
    return bad_zip_path

def test_is_bad_zip_with_single_file_zip(single_file_zip):
    assert not _is_bad_zip(single_file_zip), "Single file zip should not be considered bad."

def test_is_bad_zip_with_multi_file_zip(multi_file_zip):
    assert _is_bad_zip(multi_file_zip), "Multi file zip should be considered bad."

def test_is_bad_zip_with_bad_zip(bad_zip):
    assert not _is_bad_zip(bad_zip), "Invalid zip file should not be considered bad."
