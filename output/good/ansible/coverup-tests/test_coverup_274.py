# file lib/ansible/parsing/dataloader.py:82-106
# lines [82, 85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106]
# branches ['90->91', '90->94', '102->103', '102->106']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display
from ansible.module_utils._text import to_text
import tempfile
import os
import json
import yaml

# Mock the Display class to prevent actual printing to stdout during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.parsing.dataloader.Display', return_value=mocker.Mock(spec=Display))

# Test function to improve coverage
def test_load_from_file_with_cache_and_unsafe(mock_display, mocker):
    # Create a temporary file to simulate a real file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b'{"mock_key": "mock_value"}')
        tmp_filename = tmp.name

    # Ensure the file is deleted after the test
    try:
        # Mock the DataLoader methods used in load_from_file
        mocker.patch.object(DataLoader, 'path_dwim', return_value=tmp_filename)
        mocker.patch.object(DataLoader, '_get_file_contents', return_value=(b'{"mock_key": "mock_value"}', True))
        mocker.patch('ansible.parsing.dataloader.copy.deepcopy', side_effect=lambda x: x)

        # Create DataLoader instance and call load_from_file with cache=True and unsafe=True
        loader = DataLoader()
        loader._FILE_CACHE = {}  # Reset file cache for the test
        result = loader.load_from_file(tmp_filename, cache=True, unsafe=True)

        # Assert that the result is as expected and cache is used
        assert result == {'mock_key': 'mock_value'}
        assert tmp_filename in loader._FILE_CACHE

        # Call load_from_file again to hit the cache branch
        cached_result = loader.load_from_file(tmp_filename, cache=True, unsafe=True)
        assert cached_result == {'mock_key': 'mock_value'}

        # Assert that the cache was indeed used
        assert DataLoader._get_file_contents.call_count == 1  # _get_file_contents should only be called once, second call hits cache

    finally:
        # Clean up the temporary file
        os.remove(tmp_filename)
