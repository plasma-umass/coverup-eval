# file lib/ansible/parsing/dataloader.py:286-343
# lines [298, 299, 301, 302, 303, 304, 305, 307, 308, 309, 311, 312, 313, 314, 315, 318, 319, 320, 323, 324, 325, 329, 330, 331, 333, 334, 335, 336, 337, 338, 340, 341, 343]
# branches ['303->304', '303->305', '305->307', '305->311', '308->309', '308->340', '312->313', '312->329', '318->319', '318->323', '323->324', '323->325', '329->330', '329->331', '334->335', '334->340', '336->334', '336->337', '340->341', '340->343']

import os
import pytest
from ansible.errors import AnsibleFileNotFound
from ansible.parsing.dataloader import DataLoader
from ansible.utils.path import unfrackpath
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'warning')
    mocker.patch.object(Display, 'debug')
    mocker.patch.object(Display, 'vvvvv')

@pytest.fixture
def temp_dir(tmp_path):
    # Create a temporary directory and file for testing
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    file_path = dir_path / "test_file.txt"
    file_path.write_text("content")
    return str(dir_path)

def test_path_dwim_relative_stack(mock_display, temp_dir):
    dataloader = DataLoader()

    # Set up the paths to include the temporary directory
    paths = [temp_dir]
    dirname = "test_dir"
    source = "test_file.txt"

    # Test the function with a valid file path
    result = dataloader.path_dwim_relative_stack(paths, dirname, source)
    expected_path = os.path.join(temp_dir, source)
    assert result == expected_path, "The result should be the absolute path to the source file"

    # Test the function with a non-existent file, expecting an exception
    with pytest.raises(AnsibleFileNotFound):
        dataloader.path_dwim_relative_stack(paths, dirname, "non_existent_file.txt")

    # Test the function with an absolute path
    absolute_path = os.path.join(temp_dir, source)
    result = dataloader.path_dwim_relative_stack(paths, dirname, absolute_path)
    assert result == absolute_path, "The result should be the absolute path to the source file"

    # Test the function with a tilde in the source path
    home_dir = os.path.expanduser("~")
    tilde_path = os.path.join(home_dir, source)
    with open(tilde_path, 'w') as f:
        f.write("content")
    try:
        result = dataloader.path_dwim_relative_stack(paths, dirname, tilde_path)
        assert result == tilde_path, "The result should be the tilde-expanded path to the source file"
    finally:
        os.remove(tilde_path)

    # Test the function with a null source value
    with pytest.raises(AnsibleFileNotFound):
        dataloader.path_dwim_relative_stack(paths, dirname, None)

    # Test the function with a source value that starts with a directory separator
    sep_path = os.path.join(os.sep, temp_dir, source)
    with open(sep_path, 'w') as f:
        f.write("content")
    try:
        result = dataloader.path_dwim_relative_stack(paths, dirname, sep_path)
        assert result == sep_path, "The result should be the path to the source file with a directory separator"
    finally:
        os.remove(sep_path)
