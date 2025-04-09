# file: isort/format.py:111-134
# asked: {"lines": [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}
# gained: {"lines": [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}

import pytest
from io import StringIO
import re
from isort.format import ColoramaPrinter

# Mocking colorama for the test
class MockColorama:
    class Fore:
        RED = '\033[31m'
        GREEN = '\033[32m'
    class Style:
        RESET_ALL = '\033[0m'

@pytest.fixture
def mock_colorama(monkeypatch):
    monkeypatch.setattr("isort.format.colorama", MockColorama)

@pytest.fixture
def colorama_printer(mock_colorama):
    output = StringIO()
    return ColoramaPrinter(output=output), output

def test_colorama_printer_init(colorama_printer):
    printer, output = colorama_printer
    assert printer.ERROR == '\033[31mERROR\033[0m'
    assert printer.SUCCESS == '\033[32mSUCCESS\033[0m'
    assert printer.ADDED_LINE == '\033[32m'
    assert printer.REMOVED_LINE == '\033[31m'

def test_style_text_with_style(colorama_printer):
    printer, output = colorama_printer
    styled_text = printer.style_text("Test", MockColorama.Fore.RED)
    assert styled_text == '\033[31mTest\033[0m'

def test_style_text_without_style(colorama_printer):
    printer, output = colorama_printer
    styled_text = printer.style_text("Test")
    assert styled_text == "Test"

def test_diff_line_added(colorama_printer):
    printer, output = colorama_printer
    added_line = "+ This is an added line"
    printer.diff_line(added_line)
    assert output.getvalue() == '\033[32m+ This is an added line\033[0m'

def test_diff_line_removed(colorama_printer):
    printer, output = colorama_printer
    removed_line = "- This is a removed line"
    printer.diff_line(removed_line)
    assert output.getvalue() == '\033[31m- This is a removed line\033[0m'

def test_diff_line_no_change(colorama_printer):
    printer, output = colorama_printer
    unchanged_line = "  This is an unchanged line"
    printer.diff_line(unchanged_line)
    assert output.getvalue() == "  This is an unchanged line"
