# file mimesis/providers/path.py:41-49
# lines [41, 49]
# branches []

import pytest
from mimesis.providers.path import Path

def test_root(mocker):
    # Mock the _pathlib_home attribute to control its behavior
    mock_path = mocker.Mock()
    mock_path.parent = "/mocked/root"
    
    # Create an instance of the Path provider
    path_provider = Path()
    
    # Patch the _pathlib_home attribute
    mocker.patch.object(path_provider, '_pathlib_home', mock_path)
    
    # Call the root method and assert the expected result
    result = path_provider.root()
    assert result == "/mocked/root"
