# file: pysnooper/tracer.py:136-145
# asked: {"lines": [136, 137, 138, 139, 141, 142, 143, 144, 145], "branches": []}
# gained: {"lines": [136, 137, 138, 139, 141, 142, 143, 144, 145], "branches": []}

import pytest
import os
from pysnooper import pycompat
from pysnooper.tracer import FileWriter

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_file.txt"
    yield file
    if file.exists():
        file.unlink()

def test_file_writer_overwrite(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line"
    writer.overwrite = True  # Ensure overwrite is set to True before writing again
    writer.write("Second line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Second line"

def test_file_writer_append(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line\n")
    writer.overwrite = False
    writer.write("Second line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line\nSecond line"

def test_file_writer_initial_overwrite(temp_file):
    writer = FileWriter(temp_file, overwrite=True)
    writer.write("First line")
    writer.overwrite = True
    writer.write("Second line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Second line"
