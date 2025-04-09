# file lib/ansible/parsing/dataloader.py:175-179
# lines [175, 178, 179]
# branches ['178->exit', '178->179']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text

# Test function to cover DataLoader.set_basedir
def test_set_basedir(tmp_path):
    # Create a DataLoader instance
    data_loader = DataLoader()

    # Use a temporary directory as the base directory
    temp_basedir = tmp_path / "base_dir"
    temp_basedir.mkdir()

    # Call set_basedir with the temporary directory
    data_loader.set_basedir(str(temp_basedir))

    # Check if the base directory is set correctly
    assert data_loader._basedir == to_text(str(temp_basedir))

    # Call set_basedir with None to test the None branch
    data_loader.set_basedir(None)

    # Check if the base directory remains unchanged
    assert data_loader._basedir == to_text(str(temp_basedir))
