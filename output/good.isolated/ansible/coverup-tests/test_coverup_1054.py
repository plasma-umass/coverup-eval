# file lib/ansible/parsing/dataloader.py:171-173
# lines [171, 173]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader

# Test function to cover get_basedir method
def test_get_basedir():
    # Create an instance of DataLoader
    data_loader = DataLoader()

    # Set the _basedir attribute to a known value
    expected_basedir = '/some/fake/path'
    data_loader._basedir = expected_basedir

    # Call get_basedir and assert the result is as expected
    result = data_loader.get_basedir()
    assert result == expected_basedir, "get_basedir did not return the expected basedir"
