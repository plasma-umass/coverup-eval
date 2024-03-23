# file pytutils/lazy/lazy_import.py:304-309
# lines [304, 305, 306, 307, 309]
# branches ['306->307', '306->309']

import pytest
from unittest.mock import MagicMock
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def mock_import_replacer(mocker):
    return mocker.patch('pytutils.lazy.lazy_import.ImportReplacer')

def test_import_processor_init_with_default_lazy_import_class():
    processor = ImportProcessor()
    assert processor._lazy_import_class.__name__ == 'ImportReplacer'

def test_import_processor_init_with_custom_lazy_import_class(mock_import_replacer):
    mock_lazy_import_class = MagicMock()
    processor = ImportProcessor(lazy_import_class=mock_lazy_import_class)
    assert processor._lazy_import_class == mock_lazy_import_class
