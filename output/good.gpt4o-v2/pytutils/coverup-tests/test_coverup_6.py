# file: pytutils/lazy/lazy_import.py:304-309
# asked: {"lines": [304, 305, 306, 307, 309], "branches": [[306, 307], [306, 309]]}
# gained: {"lines": [304, 305, 306, 307, 309], "branches": [[306, 307], [306, 309]]}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

def test_import_processor_default_lazy_import_class():
    processor = ImportProcessor()
    assert processor._lazy_import_class == ImportReplacer

def test_import_processor_custom_lazy_import_class():
    class CustomImportReplacer:
        pass

    processor = ImportProcessor(lazy_import_class=CustomImportReplacer)
    assert processor._lazy_import_class == CustomImportReplacer
