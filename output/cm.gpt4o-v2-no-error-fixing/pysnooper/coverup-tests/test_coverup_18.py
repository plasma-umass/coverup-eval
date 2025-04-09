# file: pysnooper/tracer.py:136-145
# asked: {"lines": [138, 139, 142, 143, 144, 145], "branches": []}
# gained: {"lines": [138, 139, 142, 143, 144, 145], "branches": []}

import pytest
from pysnooper.tracer import FileWriter
import os

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_file.txt"

def test_file_writer_initialization(temp_file):
    writer = FileWriter(temp_file, True)
    assert writer.path == str(temp_file)
    assert writer.overwrite is True

def test_file_writer_write_overwrite(temp_file):
    writer = FileWriter(temp_file, True)
    writer.write("Hello, World!")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Hello, World!"
    assert writer.overwrite is False

def test_file_writer_write_append(temp_file):
    writer = FileWriter(temp_file, True)
    writer.write("Hello, World!")
    writer.write(" Goodbye, World!")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Hello, World! Goodbye, World!"
    assert writer.overwrite is False
