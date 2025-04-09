# file: isort/format.py:94-108
# asked: {"lines": [102, 105, 108], "branches": []}
# gained: {"lines": [102, 105, 108], "branches": []}

import pytest
import sys
from io import StringIO
from isort.format import BasicPrinter

def test_basic_printer_init_default():
    printer = BasicPrinter()
    assert printer.output == sys.stdout

def test_basic_printer_init_custom_output():
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    assert printer.output == custom_output

def test_basic_printer_success_default_output(monkeypatch):
    custom_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', custom_output)
    printer = BasicPrinter()
    printer.success("Test message")
    assert custom_output.getvalue() == "SUCCESS: Test message\n"

def test_basic_printer_success_custom_output():
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    printer.success("Test message")
    assert custom_output.getvalue() == "SUCCESS: Test message\n"

def test_basic_printer_error(monkeypatch):
    custom_error = StringIO()
    monkeypatch.setattr(sys, 'stderr', custom_error)
    printer = BasicPrinter()
    printer.error("Test error")
    assert custom_error.getvalue() == "ERROR: Test error\n"

def test_basic_printer_diff_line():
    custom_output = StringIO()
    printer = BasicPrinter(output=custom_output)
    printer.diff_line("Test line")
    assert custom_output.getvalue() == "Test line"
