# file isort/format.py:44-74
# lines [44, 49, 50, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74]
# branches ['73->exit', '73->74']

import pytest
from isort.format import show_unified_diff
from unittest.mock import MagicMock
import os

@pytest.fixture
def mock_file(tmp_path):
    file = tmp_path / "test_file.py"
    file.write_text("original content")
    return file

@pytest.fixture
def mock_printer(mocker):
    printer = MagicMock()
    mocker.patch('isort.format.create_terminal_printer', return_value=printer)
    return printer

def test_show_unified_diff_with_file_path(mock_file, mock_printer):
    file_input = "original content"
    file_output = "modified content"
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=mock_file,
        color_output=True
    )
    mock_printer.diff_line.assert_called()
    assert any(call[0][0].startswith("--- ") for call in mock_printer.diff_line.call_args_list)

def test_show_unified_diff_without_file_path(mock_printer):
    file_input = "original content"
    file_output = "modified content"
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=None,
        color_output=False
    )
    mock_printer.diff_line.assert_called()
    assert any(call[0][0].startswith("--- ") for call in mock_printer.diff_line.call_args_list)

# Clean up any created files
def teardown_function(function):
    if os.path.exists("test_file.py"):
        os.remove("test_file.py")
