# file isort/format.py:111-134
# lines [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134]
# branches ['124->125', '124->126', '130->131', '130->132', '132->133', '132->134']

import re
from io import StringIO
import pytest
import colorama

from isort.format import ColoramaPrinter

ADDED_LINE_PATTERN = r"^\+.*"
REMOVED_LINE_PATTERN = r"^-.*"

@pytest.fixture
def mock_colorama(mocker):
    mocker.patch.object(colorama.Fore, 'GREEN', 'green')
    mocker.patch.object(colorama.Fore, 'RED', 'red')
    mocker.patch.object(colorama.Style, 'RESET_ALL', 'reset')

def test_colorama_printer_diff_line(mock_colorama):
    printer = ColoramaPrinter(output=StringIO())

    added_line = "+ This is an added line."
    removed_line = "- This is a removed line."
    neutral_line = "This is a neutral line."

    printer.diff_line(added_line)
    printer.diff_line(removed_line)
    printer.diff_line(neutral_line)

    printer.output.seek(0)
    output_lines = printer.output.read()

    assert 'green' + added_line + 'reset' in output_lines
    assert 'red' + removed_line + 'reset' in output_lines
    assert neutral_line in output_lines
