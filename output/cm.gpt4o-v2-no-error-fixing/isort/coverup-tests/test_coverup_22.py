# file: isort/format.py:111-134
# asked: {"lines": [113, 117, 118, 119, 120, 124, 125, 126, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}
# gained: {"lines": [113, 117, 118, 119, 120, 124, 125, 126, 129, 130, 131, 132, 133, 134], "branches": [[124, 125], [124, 126], [130, 131], [130, 132], [132, 133], [132, 134]]}

import pytest
import re
from io import StringIO
from isort.format import ColoramaPrinter
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

def test_style_text_with_style(colorama_printer):
    printer, output = colorama_printer
    styled_text = printer.style_text("test", colorama.Fore.BLUE)
    assert styled_text == colorama.Fore.BLUE + "test" + colorama.Style.RESET_ALL

def test_style_text_without_style(colorama_printer):
    printer, output = colorama_printer
    styled_text = printer.style_text("test")
    assert styled_text == "test"

def test_diff_line_added(colorama_printer):
    printer, output = colorama_printer
    printer.diff_line("+ added line")
    assert output.getvalue() == colorama.Fore.GREEN + "+ added line" + colorama.Style.RESET_ALL

def test_diff_line_removed(colorama_printer):
    printer, output = colorama_printer
    printer.diff_line("- removed line")
    assert output.getvalue() == colorama.Fore.RED + "- removed line" + colorama.Style.RESET_ALL

def test_diff_line_no_match(colorama_printer):
    printer, output = colorama_printer
    printer.diff_line(" no match line")
    assert output.getvalue() == " no match line"
