# file: isort/format.py:94-108
# asked: {"lines": [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108], "branches": []}
# gained: {"lines": [94, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108], "branches": []}

import pytest
import sys
from io import StringIO
from isort.format import BasicPrinter

def test_basic_printer_init():
    # Test default initialization
    printer = BasicPrinter()
    assert printer.output == sys.stdout

    # Test initialization with custom output
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    assert printer.output == custom_output

def test_basic_printer_success():
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    printer.success("Test message")
    assert custom_output.getvalue() == "SUCCESS: Test message\n"

def test_basic_printer_error(monkeypatch):
    custom_stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', custom_stderr)
    printer = BasicPrinter()
    printer.error("Test error message")
    assert custom_stderr.getvalue() == "ERROR: Test error message\n"

def test_basic_printer_diff_line():
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    printer.diff_line("Test diff line")
    assert custom_output.getvalue() == "Test diff line"
