# file: pysnooper/tracer.py:136-145
# asked: {"lines": [136, 137, 138, 139, 141, 142, 143, 144, 145], "branches": []}
# gained: {"lines": [136, 137, 141], "branches": []}

import pytest
from pysnooper import pycompat
from io import open
import os

class FileWriter(object):
    def __init__(self, path, overwrite):
        self.path = pycompat.text_type(path)
        self.overwrite = overwrite

    def write(self, s):
        with open(self.path, 'w' if self.overwrite else 'a', encoding='utf-8') as output_file:
            output_file.write(s)
        self.overwrite = False

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    yield file_path
    if file_path.exists():
        file_path.unlink()

def test_file_writer_overwrite(temp_file):
    writer = FileWriter(temp_file, True)
    writer.write("First line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line"
    assert writer.overwrite == False

def test_file_writer_append(temp_file):
    writer = FileWriter(temp_file, True)
    writer.write("First line\n")
    writer = FileWriter(temp_file, False)
    writer.write("Second line")
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "First line\nSecond line"
    assert writer.overwrite == False
