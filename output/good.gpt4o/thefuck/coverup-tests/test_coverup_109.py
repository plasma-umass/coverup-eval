# file thefuck/rules/cat_dir.py:5-10
# lines [5, 6, 7, 8, 9]
# branches []

import os
import pytest
from unittest.mock import MagicMock
from thefuck.rules.cat_dir import match
from thefuck.types import Command

@pytest.fixture
def mock_command():
    command = Command(script='cat test_dir', output='cat: some error message')
    return command

def test_match_cat_dir(mock_command, mocker):
    # Create a temporary directory for testing
    test_dir = 'test_dir'
    os.mkdir(test_dir)
    
    try:
        # Mock os.path.isdir to return True for the test directory
        mocker.patch('os.path.isdir', return_value=True)
        
        # Assert that the match function returns True
        assert match(mock_command) is True
    finally:
        # Clean up the temporary directory
        os.rmdir(test_dir)

def test_match_cat_dir_no_match(mock_command, mocker):
    # Create a temporary directory for testing
    test_dir = 'test_dir'
    os.mkdir(test_dir)
    
    try:
        # Modify the command output to not match the condition
        mock_command = Command(script='cat test_dir', output='some other message')
        
        # Mock os.path.isdir to return True for the test directory
        mocker.patch('os.path.isdir', return_value=True)
        
        # Assert that the match function returns False
        assert match(mock_command) is False
    finally:
        # Clean up the temporary directory
        os.rmdir(test_dir)
