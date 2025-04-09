# file lib/ansible/utils/collection_loader/_collection_finder.py:328-330
# lines [328, 330]
# branches []

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
from ansible.module_utils._text import to_bytes

# Assuming the existence of a fixture that creates a temporary directory
@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path

class MockedAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        # Mock the __init__ to not require any arguments
        pass

def test_get_subpackage_search_paths(temp_dir, mocker):
    # Create a mock for to_bytes that just returns the path
    mocker.patch('ansible.module_utils._text.to_bytes', side_effect=lambda p: p)

    # Create some directories and files to act as candidate paths
    existing_dir = temp_dir / "existing_dir"
    existing_dir.mkdir()
    non_existing_dir = temp_dir / "non_existing_dir"
    existing_file = temp_dir / "existing_file.txt"
    existing_file.touch()

    # Instantiate the mocked loader base class
    loader_base = MockedAnsibleCollectionPkgLoaderBase()

    # Define candidate paths including the existing directory, non-existing directory, and a file
    candidate_paths = [str(existing_dir), str(non_existing_dir), str(existing_file)]

    # Call the method under test
    valid_paths = loader_base._get_subpackage_search_paths(candidate_paths)

    # Assert that only the existing directory is returned
    assert valid_paths == [str(existing_dir)]

    # Cleanup is handled by the temp_dir fixture
