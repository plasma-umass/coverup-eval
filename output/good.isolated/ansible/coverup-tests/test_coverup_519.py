# file lib/ansible/parsing/dataloader.py:409-418
# lines [409, 414, 415, 416, 417, 418]
# branches ['414->exit', '414->415']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display
from ansible.module_utils._text import to_text

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch('ansible.parsing.dataloader.display', autospec=True)
    display_mock.warning = mocker.MagicMock()
    return display_mock

# Test function to improve coverage
def test_cleanup_all_tmp_files_exception_handling(mock_display, tmp_path, mocker):
    # Create a DataLoader instance
    data_loader = DataLoader()

    # Create a temporary file and add it to the DataLoader's _tempfiles set
    temp_file = tmp_path / "tempfile"
    temp_file.write_text("temporary content")
    data_loader._tempfiles.add(str(temp_file))

    # Mock the cleanup_tmp_file method to raise an exception
    mocker.patch.object(data_loader, 'cleanup_tmp_file', side_effect=Exception("Mocked exception"))

    # Call the method under test
    data_loader.cleanup_all_tmp_files()

    # Assert that the warning was called with the expected message
    mock_display.warning.assert_called_once_with(
        "Unable to cleanup temp files: %s" % to_text("Mocked exception")
    )

    # Assert that the temporary file still exists (since cleanup failed)
    assert temp_file.exists()
