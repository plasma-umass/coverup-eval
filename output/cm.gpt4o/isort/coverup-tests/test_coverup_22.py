# file isort/format.py:111-134
# lines [111, 112, 113, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134]
# branches ['124->125', '124->126', '130->131', '130->132', '132->133', '132->134']

import pytest
from io import StringIO
import re
from unittest.mock import patch
from typing import Optional, TextIO

# Assuming the following constants are defined somewhere in the module
ADDED_LINE_PATTERN = r'^\+.*'
REMOVED_LINE_PATTERN = r'^\-.*'

# Mocking colorama for the purpose of this test
class MockColorama:
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
    class Style:
        RESET_ALL = '\033[0m'

# Mocking BasicPrinter for the purpose of this test
class BasicPrinter:
    def __init__(self, output: Optional[TextIO] = None):
        self.output = output or StringIO()

@pytest.fixture
def mock_colorama():
    with patch('isort.format.colorama', new=MockColorama):
        yield

def test_colorama_printer(mock_colorama):
    from isort.format import ColoramaPrinter

    output = StringIO()
    printer = ColoramaPrinter(output=output)

    # Test style_text method
    assert printer.style_text("test", MockColorama.Fore.RED) == '\033[91mtest\033[0m'
    assert printer.style_text("test") == 'test'

    # Test diff_line method with added line
    printer.diff_line("+ added line")
    assert output.getvalue() == '\033[92m+ added line\033[0m'
    output.truncate(0)
    output.seek(0)

    # Test diff_line method with removed line
    printer.diff_line("- removed line")
    assert output.getvalue() == '\033[91m- removed line\033[0m'
    output.truncate(0)
    output.seek(0)

    # Test diff_line method with no match
    printer.diff_line(" no change")
    assert output.getvalue() == ' no change'
    output.truncate(0)
    output.seek(0)
