# file: pysnooper/tracer.py:136-145
# asked: {"lines": [136, 137, 138, 139, 141, 142, 143, 144, 145], "branches": []}
# gained: {"lines": [136, 137, 138, 139, 141, 142, 143, 144, 145], "branches": []}

import pytest
from pysnooper.tracer import FileWriter
import os

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_file.txt"

def test_file_writer_overwrite(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line\n")
    
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("Second line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == "Second line\n"

def test_file_writer_append(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line\n")
    
    writer = FileWriter(temp_file, overwrite=False)
    writer.write("Second line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == "First line\nSecond line\n"

def test_file_writer_initial_overwrite_then_append(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line\n")
    
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("Second line\n")
    
    writer = FileWriter(temp_file, overwrite=False)
    writer.write("Third line\n")
    
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == "Second line\nThird line\n"
