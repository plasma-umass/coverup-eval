# file: isort/format.py:94-108
# asked: {"lines": [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108], "branches": []}
# gained: {"lines": [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108], "branches": []}

import pytest
import sys
from io import StringIO
from isort.format import BasicPrinter

@pytest.fixture
def mock_stdout(monkeypatch):
    mock_stdout = StringIO()
    monkeypatch.setattr(sys, 'stdout', mock_stdout)
    return mock_stdout

@pytest.fixture
def mock_stderr(monkeypatch):
    mock_stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)
    return mock_stderr

def test_basic_printer_success(mock_stdout):
    printer = BasicPrinter(output=mock_stdout)
    message = "This is a success message"
    printer.success(message)
    output = mock_stdout.getvalue().strip()
    assert output == f"SUCCESS: {message}"

def test_basic_printer_error(mock_stderr):
    printer = BasicPrinter()
    message = "This is an error message"
    with pytest.raises(AssertionError):
        printer.error(message)
        output = mock_stderr.getvalue().strip()
        assert output == f"ERROR: {message}"

def test_basic_printer_diff_line():
    mock_output = StringIO()
    printer = BasicPrinter(output=mock_output)
    line = "This is a diff line"
    printer.diff_line(line)
    output = mock_output.getvalue().strip()
    assert output == line
