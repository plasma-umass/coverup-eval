# file lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# lines [1029, 1034]
# branches ['1026->1029', '1033->1034']

import os
import pytest
from ansible.utils.collection_loader import _collection_finder

@pytest.fixture
def mock_os_path(mocker):
    mocker.patch.object(os.path, 'isdir', return_value=False)

def test_iter_modules_impl_nonexistent_directory(mock_os_path, tmp_path):
    # Create a temporary directory and file to test the iteration
    temp_dir = tmp_path / "nonexistent"
    temp_dir.mkdir()
    temp_file = temp_dir / "test_module.py"
    temp_file.touch()

    # Convert the temporary path to a string to pass to the function
    temp_dir_str = str(temp_dir)

    # Call the function with the temporary directory
    modules = list(_collection_finder._iter_modules_impl([temp_dir_str]))

    # Assert that the function did not yield any modules since the directory does not exist
    assert len(modules) == 0

    # Cleanup
    temp_file.unlink()
    temp_dir.rmdir()
