# file pytutils/lazy/lazy_import.py:449-475
# lines [449, 474, 475]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the ImportProcessor class is defined somewhere in the pytutils.lazy.lazy_import module
from pytutils.lazy.lazy_import import lazy_import, ImportProcessor

@pytest.fixture
def mock_import_processor(mocker):
    # Mock the ImportProcessor class
    mock_proc = mocker.MagicMock(spec=ImportProcessor)
    mock_import_processor_class = mocker.patch('pytutils.lazy.lazy_import.ImportProcessor', return_value=mock_proc)
    return mock_proc, mock_import_processor_class

def test_lazy_import(mock_import_processor):
    mock_proc, mock_import_processor_class = mock_import_processor
    # Define a scope and text for the lazy_import function
    scope = {}
    text = '''
    from some_module import some_function
    import another_module
    '''
    
    # Call the lazy_import function with the mocked ImportProcessor
    lazy_import(scope, text)
    
    # Assert that the ImportProcessor was instantiated once
    mock_import_processor_class.assert_called_once_with(lazy_import_class=None)
    
    # Assert that the lazy_import method of the ImportProcessor instance was called with the correct arguments
    mock_proc.lazy_import.assert_called_once_with(scope, text)
    
    # Assert that the scope is not modified by the lazy_import function
    assert scope == {}
