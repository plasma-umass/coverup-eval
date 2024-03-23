# file lib/ansible/parsing/dataloader.py:108-110
# lines [108, 109, 110]
# branches []

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

# Assuming the DataLoader class is part of a larger file, we import it for testing

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "temp_file.txt"
    file.write_text("This is a temporary file.")
    return str(file)

def test_path_exists_true(dataloader, temp_file):
    assert dataloader.path_exists(temp_file) == True

def test_path_exists_false(dataloader, temp_file):
    os.remove(temp_file)
    assert dataloader.path_exists(temp_file) == False
