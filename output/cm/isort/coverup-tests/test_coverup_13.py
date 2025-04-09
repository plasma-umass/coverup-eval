# file isort/format.py:94-108
# lines [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108]
# branches []

import sys
from io import StringIO
from unittest.mock import patch
import pytest

from isort.format import BasicPrinter

@pytest.fixture
def mock_stdout():
    return StringIO()

@pytest.fixture
def mock_stderr():
    return StringIO()

def test_basic_printer_success(mock_stdout):
    with patch('sys.stdout', new=mock_stdout):
        printer = BasicPrinter()
        printer.success("Test message")
        assert mock_stdout.getvalue() == "SUCCESS: Test message\n"

def test_basic_printer_error(mock_stderr):
    with patch('sys.stderr', new=mock_stderr):
        printer = BasicPrinter()
        printer.error("Test error")
        assert mock_stderr.getvalue() == "ERROR: Test error\n"

def test_basic_printer_diff_line(mock_stdout):
    with patch('sys.stdout', new=mock_stdout):
        printer = BasicPrinter()
        printer.diff_line("Diff line content")
        assert mock_stdout.getvalue() == "Diff line content"
