# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}
# gained: {"lines": [886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}

import os
import pytest

from ansible.module_utils.urls import atexit_remove_file

@pytest.fixture
def create_temp_file(tmp_path):
    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("Temporary file content")
    yield temp_file
    if temp_file.exists():
        temp_file.unlink()

def test_atexit_remove_file_exists(create_temp_file):
    temp_file = create_temp_file
    assert temp_file.exists()
    atexit_remove_file(str(temp_file))
    assert not temp_file.exists()

def test_atexit_remove_file_not_exists(tmp_path):
    non_existent_file = tmp_path / "non_existent_file.txt"
    assert not non_existent_file.exists()
    atexit_remove_file(str(non_existent_file))
    assert not non_existent_file.exists()

def test_atexit_remove_file_unlink_exception(monkeypatch, create_temp_file):
    temp_file = create_temp_file

    def mock_unlink(filename):
        raise PermissionError("Mocked permission error")

    monkeypatch.setattr(os, "unlink", mock_unlink)
    assert temp_file.exists()
    atexit_remove_file(str(temp_file))
    assert temp_file.exists()
