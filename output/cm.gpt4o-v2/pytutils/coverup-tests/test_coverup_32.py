# file: pytutils/lazy/lazy_import.py:311-318
# asked: {"lines": [317, 318], "branches": []}
# gained: {"lines": [317, 318], "branches": []}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def import_processor():
    return ImportProcessor()

def test_lazy_import_build_map_and_convert_imports(import_processor, mocker):
    # Mock the methods _build_map and _convert_imports to track their calls
    mocker.patch('pytutils.lazy.lazy_import.ImportProcessor._build_map')
    mocker.patch('pytutils.lazy.lazy_import.ImportProcessor._convert_imports')

    # Define a sample text and scope
    sample_text = "import os\nfrom sys import path"
    sample_scope = {}

    # Call the lazy_import method
    import_processor.lazy_import(sample_scope, sample_text)

    # Assert that _build_map and _convert_imports were called with correct arguments
    import_processor._build_map.assert_called_once_with(sample_text)
    import_processor._convert_imports.assert_called_once_with(sample_scope)
