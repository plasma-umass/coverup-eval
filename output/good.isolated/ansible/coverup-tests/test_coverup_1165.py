# file lib/ansible/parsing/dataloader.py:197-229
# lines [200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229]
# branches ['226->227', '226->229']

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.utils.path import unfrackpath
from ansible.module_utils._text import to_bytes

@pytest.fixture
def temp_role_dir(tmp_path):
    role_dir = tmp_path / "testrole"
    role_dir.mkdir()
    tasks_dir = role_dir / "tasks"
    tasks_dir.mkdir()
    meta_dir = role_dir / "meta"
    meta_dir.mkdir()
    (tasks_dir / "main.yml").touch()
    (meta_dir / "main.yml").touch()
    return str(role_dir)

def test_is_role_with_role_structure(temp_role_dir, mocker):
    # Mock os.path.exists to only return True for the paths we expect
    def mock_exists(path):
        path = path.decode('utf-8')  # Convert bytes to str for comparison
        return any(os.path.basename(path) == p for p in ["main.yml", "main.yaml", "main"])

    mocker.patch('os.path.exists', side_effect=mock_exists)

    # Create a DataLoader instance and call _is_role
    loader = DataLoader()
    assert loader._is_role(temp_role_dir) == True

    # Cleanup
    mocker.stopall()
