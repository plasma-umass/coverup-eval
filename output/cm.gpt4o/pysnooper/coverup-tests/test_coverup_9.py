# file pysnooper/tracer.py:136-145
# lines [136, 137, 138, 139, 141, 142, 143, 144, 145]
# branches []

import pytest
import os
from unittest import mock

# Assuming the FileWriter class is imported from pysnooper.tracer
from pysnooper.tracer import FileWriter

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    yield file_path
    if file_path.exists():
        file_path.unlink()

def test_file_writer_overwrite(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line\n"
    
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("Second line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Second line\n"

def test_file_writer_append(temp_file):
    writer = FileWriter(temp_file, overwrite=False)
    writer.write("First line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line\n"
    
    writer.write("Second line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line\nSecond line\n"
