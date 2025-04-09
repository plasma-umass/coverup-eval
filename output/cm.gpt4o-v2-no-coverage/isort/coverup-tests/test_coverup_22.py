# file: isort/format.py:44-74
# asked: {"lines": [60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}
# gained: {"lines": [60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}

import pytest
from io import StringIO
from pathlib import Path
from datetime import datetime
from unittest.mock import MagicMock, patch
from isort.format import show_unified_diff

class MockPrinter:
    def __init__(self, output):
        self.output = output
        self.lines = []

    def diff_line(self, line):
        self.lines.append(line)

def test_show_unified_diff_no_file_path():
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    output = StringIO()
    mock_printer = MockPrinter(output)

    with patch('isort.format.create_terminal_printer', return_value=mock_printer):
        show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output, color_output=False)

    assert len(mock_printer.lines) > 0
    assert "--- :before" in mock_printer.lines[0]
    assert "+++ :after" in mock_printer.lines[1]

def test_show_unified_diff_with_file_path(tmp_path):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(file_input)
    output = StringIO()
    mock_printer = MockPrinter(output)

    with patch('isort.format.create_terminal_printer', return_value=mock_printer):
        show_unified_diff(file_input=file_input, file_output=file_output, file_path=test_file, output=output, color_output=False)

    assert len(mock_printer.lines) > 0
    assert f"--- {test_file}:before" in mock_printer.lines[0]
    assert f"+++ {test_file}:after" in mock_printer.lines[1]

def test_show_unified_diff_color_output():
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 modified\n"
    output = StringIO()
    mock_printer = MockPrinter(output)

    with patch('isort.format.create_terminal_printer', return_value=mock_printer):
        show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output, color_output=True)

    assert len(mock_printer.lines) > 0
    assert "--- :before" in mock_printer.lines[0]
    assert "+++ :after" in mock_printer.lines[1]
