# file lib/ansible/parsing/dataloader.py:82-106
# lines [106]
# branches ['102->106']

import pytest
from ansible.parsing.dataloader import DataLoader
import tempfile
import os
import json

# Mock DataLoader methods that are not under test
@pytest.fixture
def mock_data_loader_methods(mocker):
    mocker.patch.object(DataLoader, 'path_dwim', side_effect=lambda x: x)
    mocker.patch.object(DataLoader, '_get_file_contents', side_effect=lambda x: (b'{"key": "value"}', True))

# Test function to cover line 106
def test_load_from_file_unsafe_false(mock_data_loader_methods):
    # Create a temporary directory to simulate file loading
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a temporary file
        tmp_file_path = os.path.join(tmp_dir, 'test.json')
        with open(tmp_file_path, 'w') as tmp_file:
            json.dump({"key": "value"}, tmp_file)

        # Initialize DataLoader and load from file with unsafe=False
        data_loader = DataLoader()
        data_loader._FILE_CACHE = {}
        result = data_loader.load_from_file(tmp_file_path, cache=True, unsafe=False, json_only=True)

        # Assert that the result is a deepcopy (modifying it won't affect the cache)
        assert result == {"key": "value"}
        result['key'] = "new_value"
        assert data_loader._FILE_CACHE[tmp_file_path] == {"key": "value"}

        # Cleanup is handled by the TemporaryDirectory context manager
