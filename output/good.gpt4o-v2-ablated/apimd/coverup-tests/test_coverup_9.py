# file: apimd/loader.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import os
import pytest

from apimd.loader import _write

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "temp_file.txt"
    yield temp_file
    if temp_file.exists():
        temp_file.unlink()

def test_write_creates_file(temp_file):
    _write(str(temp_file), "Hello, World!")
    assert temp_file.exists()

def test_write_content(temp_file):
    content = "Hello, World!"
    _write(str(temp_file), content)
    with open(temp_file, 'r', encoding='utf-8') as f:
        assert f.read() == content

def test_write_overwrites_content(temp_file):
    initial_content = "Initial Content"
    new_content = "New Content"
    _write(str(temp_file), initial_content)
    _write(str(temp_file), new_content)
    with open(temp_file, 'r', encoding='utf-8') as f:
        assert f.read() == new_content
