# file isort/format.py:94-108
# lines [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108]
# branches []

import pytest
import sys
from io import StringIO
from isort.format import BasicPrinter

def test_basic_printer_success():
    output = StringIO()
    printer = BasicPrinter(output=output)
    printer.success("Test success message")
    assert output.getvalue() == "SUCCESS: Test success message\n"

def test_basic_printer_error(mocker):
    mock_stderr = StringIO()
    mocker.patch('sys.stderr', mock_stderr)
    printer = BasicPrinter()
    printer.error("Test error message")
    assert mock_stderr.getvalue() == "ERROR: Test error message\n"

def test_basic_printer_diff_line():
    output = StringIO()
    printer = BasicPrinter(output=output)
    printer.diff_line("Test diff line")
    assert output.getvalue() == "Test diff line"
