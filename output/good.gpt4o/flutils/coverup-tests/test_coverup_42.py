# file flutils/pathutils.py:569-571
# lines [569, 570, 571]
# branches []

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib(mocker):
    # Mock the normalize_path function to ensure it is called correctly
    mock_normalize_path = mocker.patch('flutils.pathutils.normalize_path', wraps=normalize_path)
    
    # Create a Path object
    path_obj = Path('/some/test/path')
    
    # Call the function to be tested
    result = normalize_path(path_obj)
    
    # Assert that the mock was called with the correct argument
    mock_normalize_path.assert_called_once_with('/some/test/path')
    
    # Assert that the result is as expected
    assert result == Path('/some/test/path')
