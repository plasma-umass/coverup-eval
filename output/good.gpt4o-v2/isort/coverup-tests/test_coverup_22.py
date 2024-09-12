# file: isort/format.py:44-74
# asked: {"lines": [44, 49, 50, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}
# gained: {"lines": [44, 49, 50, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}

import pytest
from io import StringIO
from pathlib import Path
from datetime import datetime
from unittest import mock
from isort.format import show_unified_diff

class MockPrinter:
    def __init__(self, output):
        self.output = output

    def diff_line(self, line):
        if self.output:
            self.output.write(line)
        else:
            print(line)

@pytest.fixture
def mock_create_terminal_printer(monkeypatch):
    def mock_printer(color, output):
        return MockPrinter(output)
    monkeypatch.setattr('isort.format.create_terminal_printer', mock_printer)

def test_show_unified_diff_no_file_path(mock_create_terminal_printer):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    output = StringIO()
    
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=None,
        output=output,
        color_output=False
    )
    
    output.seek(0)
    diff_output = output.read()
    assert "--- :before" in diff_output
    assert "+++ :after" in diff_output
    assert "@@ -1,2 +1,2 @@" in diff_output
    assert " line1\n" in diff_output
    assert "-line2\n" in diff_output
    assert "+line2 modified\n" in diff_output

def test_show_unified_diff_with_file_path(mock_create_terminal_printer, tmp_path):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(file_input)
    output = StringIO()
    
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=test_file,
        output=output,
        color_output=False
    )
    
    output.seek(0)
    diff_output = output.read()
    assert f"--- {test_file}:before" in diff_output
    assert f"+++ {test_file}:after" in diff_output
    assert "@@ -1,2 +1,2 @@" in diff_output
    assert " line1\n" in diff_output
    assert "-line2\n" in diff_output
    assert "+line2 modified\n" in diff_output

def test_show_unified_diff_with_color_output(mock_create_terminal_printer):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    output = StringIO()
    
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=None,
        output=output,
        color_output=True
    )
    
    output.seek(0)
    diff_output = output.read()
    assert "--- :before" in diff_output
    assert "+++ :after" in diff_output
    assert "@@ -1,2 +1,2 @@" in diff_output
    assert " line1\n" in diff_output
    assert "-line2\n" in diff_output
    assert "+line2 modified\n" in diff_output
