# file: isort/format.py:44-74
# asked: {"lines": [60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}
# gained: {"lines": [60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74], "branches": [[73, 0], [73, 74]]}

import pytest
from unittest.mock import MagicMock, mock_open, patch
from pathlib import Path
from datetime import datetime
from io import StringIO
from isort.format import show_unified_diff

@pytest.fixture
def mock_printer(mocker):
    return mocker.patch('isort.format.create_terminal_printer')

@pytest.fixture
def mock_path(mocker):
    mock_path = mocker.Mock(spec=Path)
    mock_path.stat.return_value.st_mtime = datetime.now().timestamp()
    return mock_path

def test_show_unified_diff_no_path_no_color(mock_printer):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 changed\n"
    file_path = None
    output = StringIO()

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=file_path,
        output=output,
        color_output=False
    )

    mock_printer.assert_called_once_with(False, output)
    printer_instance = mock_printer.return_value
    assert printer_instance.diff_line.call_count > 0

def test_show_unified_diff_with_path_no_color(mock_printer, mock_path):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 changed\n"
    output = StringIO()

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=mock_path,
        output=output,
        color_output=False
    )

    mock_printer.assert_called_once_with(False, output)
    printer_instance = mock_printer.return_value
    assert printer_instance.diff_line.call_count > 0

def test_show_unified_diff_with_path_with_color(mock_printer, mock_path):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 changed\n"
    output = StringIO()

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=mock_path,
        output=output,
        color_output=True
    )

    mock_printer.assert_called_once_with(True, output)
    printer_instance = mock_printer.return_value
    assert printer_instance.diff_line.call_count > 0

def test_show_unified_diff_no_path_with_color(mock_printer):
    file_input = "line1\nline2\n"
    file_output = "line1\nline2 changed\n"
    file_path = None
    output = StringIO()

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=file_path,
        output=output,
        color_output=True
    )

    mock_printer.assert_called_once_with(True, output)
    printer_instance = mock_printer.return_value
    assert printer_instance.diff_line.call_count > 0
