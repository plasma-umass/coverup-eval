# file: apimd/loader.py:24-27
# asked: {"lines": [24, 26, 27], "branches": []}
# gained: {"lines": [24, 26, 27], "branches": []}

import pytest
import os

from apimd.loader import _read

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "temp_script.py"
    temp_file.write_text("print('Hello, World!')")
    return temp_file

def test_read_file(temp_file):
    content = _read(str(temp_file))
    assert content == "print('Hello, World!')"

def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        _read("nonexistent_file.py")
