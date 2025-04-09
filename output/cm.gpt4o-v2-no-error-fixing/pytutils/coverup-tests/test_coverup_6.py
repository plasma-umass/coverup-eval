# file: pytutils/lazy/lazy_import.py:304-309
# asked: {"lines": [304, 305, 306, 307, 309], "branches": [[306, 307], [306, 309]]}
# gained: {"lines": [304, 305, 306, 307, 309], "branches": [[306, 307], [306, 309]]}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

def test_import_processor_with_default_class():
    processor = ImportProcessor()
    assert isinstance(processor._lazy_import_class, type)
    assert processor._lazy_import_class == ImportReplacer

def test_import_processor_with_custom_class():
    class CustomImportReplacer:
        pass

    processor = ImportProcessor(lazy_import_class=CustomImportReplacer)
    assert processor._lazy_import_class == CustomImportReplacer
