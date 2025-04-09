# file isort/format.py:44-74
# lines [60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 74]
# branches ['73->exit', '73->74']

import pytest
from io import StringIO
from pathlib import Path
from datetime import datetime
from isort.format import show_unified_diff

def test_show_unified_diff(mocker):
    # Mock create_terminal_printer to avoid actual printing
    mock_printer = mocker.Mock()
    mock_create_terminal_printer = mocker.patch('isort.format.create_terminal_printer', return_value=mock_printer)

    # Create temporary file path
    temp_file = Path("temp_file.txt")
    temp_file.touch()
    temp_file_mtime = datetime.fromtimestamp(temp_file.stat().st_mtime)

    # Define input and output strings
    file_input = "line1\nline2\nline3\n"
    file_output = "line1\nline2 modified\nline3\n"

    # Call the function
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=temp_file,
        output=None,
        color_output=False
    )

    # Assertions
    mock_create_terminal_printer.assert_called_once_with(False, None)
    mock_printer.diff_line.assert_called()  # Ensure diff_line was called

    # Clean up
    temp_file.unlink()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    temp_file = Path("temp_file.txt")
    if temp_file.exists():
        temp_file.unlink()
