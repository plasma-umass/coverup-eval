# file pytutils/lazy/lazy_import.py:311-318
# lines [311, 317, 318]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the ImportProcessor class is imported from pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def import_processor():
    return ImportProcessor()

def test_lazy_import(import_processor, mocker):
    scope = {}
    text = "import os\nimport sys"

    # Mock the _build_map and _convert_imports methods using a different approach
    mocker.patch.object(ImportProcessor, '_build_map', MagicMock())
    mocker.patch.object(ImportProcessor, '_convert_imports', MagicMock())

    import_processor.lazy_import(scope, text)

    # Assert that _build_map and _convert_imports were called with the correct arguments
    import_processor._build_map.assert_called_once_with(text)
    import_processor._convert_imports.assert_called_once_with(scope)
