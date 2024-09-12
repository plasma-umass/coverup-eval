# file: isort/format.py:111-134
# asked: {"lines": [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}
# gained: {"lines": [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}

import pytest
import re
from io import StringIO
from isort.format import ColoramaPrinter, BasicPrinter
import colorama

ADDED_LINE_PATTERN = re.compile(r'\+[^+]')
REMOVED_LINE_PATTERN = re.compile(r'-[^-]')

@pytest.fixture
def colorama_printer():
    output = StringIO()
    printer = ColoramaPrinter(output=output)
    return printer, output

def test_colorama_printer_init(colorama_printer):
    printer, output = colorama_printer
    assert printer.ERROR == colorama.Fore.RED + "ERROR" + colorama.Style.RESET_ALL
    assert printer.SUCCESS == colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL
    assert printer.ADDED_LINE == colorama.Fore.GREEN
    assert printer.REMOVED_LINE == colorama.Fore.RED

def test_colorama_printer_style_text(colorama_printer):
    printer, output = colorama_printer
    assert printer.style_text("test") == "test"
    assert printer.style_text("test", colorama.Fore.RED) == colorama.Fore.RED + "test" + colorama.Style.RESET_ALL

def test_colorama_printer_diff_line_added(colorama_printer):
    printer, output = colorama_printer
    line = "+ added line"
    printer.diff_line(line)
    assert output.getvalue() == colorama.Fore.GREEN + line + colorama.Style.RESET_ALL

def test_colorama_printer_diff_line_removed(colorama_printer):
    printer, output = colorama_printer
    line = "- removed line"
    printer.diff_line(line)
    assert output.getvalue() == colorama.Fore.RED + line + colorama.Style.RESET_ALL

def test_colorama_printer_diff_line_neutral(colorama_printer):
    printer, output = colorama_printer
    line = " neutral line"
    printer.diff_line(line)
    assert output.getvalue() == line
