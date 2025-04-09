# file lib/ansible/module_utils/facts/system/distribution.py:30-44
# lines [30, 32, 33, 36, 37, 40, 41, 44]
# branches ['32->33', '32->36', '36->37', '36->40', '40->41', '40->44']

import os
import pytest
from ansible.module_utils.facts.system.distribution import _file_exists

def test__file_exists_nonexistent(tmp_path, mocker):
    # Setup: create a fake path
    fake_path = tmp_path / "fake_file"
    assert not fake_path.exists()

    # Test: the file does not exist
    assert not _file_exists(str(fake_path))

def test__file_exists_empty_allowed(tmp_path, mocker):
    # Setup: create an empty file
    empty_file = tmp_path / "empty_file"
    empty_file.touch()
    assert empty_file.exists() and os.path.getsize(str(empty_file)) == 0

    # Test: the file exists and is empty, but empty is allowed
    assert _file_exists(str(empty_file), allow_empty=True)

def test__file_exists_empty_not_allowed(tmp_path, mocker):
    # Setup: create an empty file
    empty_file = tmp_path / "empty_file"
    empty_file.touch()
    assert empty_file.exists() and os.path.getsize(str(empty_file)) == 0

    # Test: the file exists and is empty, and empty is not allowed
    assert not _file_exists(str(empty_file), allow_empty=False)

def test__file_exists_with_content(tmp_path, mocker):
    # Setup: create a file with content
    file_with_content = tmp_path / "file_with_content"
    file_with_content.write_text("content")
    assert file_with_content.exists() and os.path.getsize(str(file_with_content)) > 0

    # Test: the file exists and has content
    assert _file_exists(str(file_with_content))
