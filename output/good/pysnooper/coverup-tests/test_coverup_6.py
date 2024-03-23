# file pysnooper/tracer.py:136-145
# lines [136, 137, 138, 139, 141, 142, 143, 144, 145]
# branches []

import os
import pytest
from pysnooper.tracer import FileWriter

@pytest.fixture
def file_writer(tmp_path):
    file_path = tmp_path / "test_file.txt"
    return FileWriter(file_path, overwrite=True), file_path

def test_file_writer_overwrite(file_writer):
    writer, file_path = file_writer
    test_content = "Initial content"
    writer.write(test_content)
    assert file_path.read_text() == test_content
    assert not writer.overwrite

def test_file_writer_append(file_writer):
    writer, file_path = file_writer
    initial_content = "Initial content"
    appended_content = "Appended content"
    writer.write(initial_content)
    writer.write(appended_content)
    assert file_path.read_text() == initial_content + appended_content
    assert not writer.overwrite
