# file: pytutils/lazy/lazy_import.py:311-318
# asked: {"lines": [311, 317, 318], "branches": []}
# gained: {"lines": [311, 317, 318], "branches": []}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def import_processor():
    return ImportProcessor()

def test_lazy_import(mocker, import_processor):
    scope = {}
    text = "import os\nimport sys"

    mock_build_map = mocker.patch("pytutils.lazy.lazy_import.ImportProcessor._build_map", autospec=True)
    mock_convert_imports = mocker.patch("pytutils.lazy.lazy_import.ImportProcessor._convert_imports", autospec=True)

    import_processor.lazy_import(scope, text)

    mock_build_map.assert_called_once_with(import_processor, text)
    mock_convert_imports.assert_called_once_with(import_processor, scope)
