# file pytutils/lazy/lazy_import.py:311-318
# lines [311, 317, 318]
# branches []

import pytest
from unittest.mock import patch

# Assuming the ImportProcessor class is part of a module named pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def import_processor():
    return ImportProcessor()

@pytest.fixture
def mock_scope():
    return {}

def test_lazy_import(import_processor, mock_scope):
    with patch.object(ImportProcessor, '_build_map') as mock_build_map, \
         patch.object(ImportProcessor, '_convert_imports') as mock_convert_imports:
        
        # Call the method under test
        import_processor.lazy_import(mock_scope, "import os")

        # Assert that the mocked methods were called with the correct arguments
        mock_build_map.assert_called_once_with("import os")
        mock_convert_imports.assert_called_once_with(mock_scope)

        # No postconditions to assert since the original methods are mocked
