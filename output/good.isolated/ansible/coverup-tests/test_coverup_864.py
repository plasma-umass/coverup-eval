# file lib/ansible/parsing/dataloader.py:124-127
# lines [124, 126, 127]
# branches []

import os
import pytest
from ansible.parsing.dataloader import DataLoader

# Assuming the DataLoader class is defined elsewhere in the module

@pytest.fixture
def temp_executable_file(tmp_path):
    exec_file = tmp_path / "executable_file"
    exec_file.write_text("#!/bin/bash\necho 'Hello World'")
    exec_file.chmod(0o755)
    yield exec_file
    exec_file.unlink()

@pytest.fixture
def temp_non_executable_file(tmp_path):
    non_exec_file = tmp_path / "non_executable_file"
    non_exec_file.write_text("I am not executable")
    non_exec_file.chmod(0o644)
    yield non_exec_file
    non_exec_file.unlink()

def test_is_executable_with_executable_file(temp_executable_file, mocker):
    mocker.patch('ansible.parsing.dataloader.is_executable', return_value=True)
    data_loader = DataLoader()
    assert data_loader.is_executable(str(temp_executable_file)) is True

def test_is_executable_with_non_executable_file(temp_non_executable_file, mocker):
    mocker.patch('ansible.parsing.dataloader.is_executable', return_value=False)
    data_loader = DataLoader()
    assert data_loader.is_executable(str(temp_non_executable_file)) is False
