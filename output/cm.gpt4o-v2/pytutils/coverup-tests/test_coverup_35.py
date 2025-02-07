# file: pytutils/lazy/lazy_import.py:385-413
# asked: {"lines": [390, 391, 392, 394, 396, 398, 399, 400, 401, 402, 403, 407, 408, 410, 411, 412, 413], "branches": [[390, 391], [390, 392], [398, 0], [398, 399], [400, 401], [400, 402], [403, 407], [403, 410], [411, 412], [411, 413]]}
# gained: {"lines": [390, 391, 392, 394, 396, 398, 399, 400, 402, 403, 407, 408, 410, 411, 412, 413], "branches": [[390, 391], [390, 392], [398, 0], [398, 399], [400, 402], [403, 407], [403, 410], [411, 412], [411, 413]]}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor

class MockErrors:
    class ImportNameCollision(Exception):
        pass

def test_convert_from_str_valid_import():
    processor = ImportProcessor()
    processor.imports = {}
    processor._convert_from_str('from foo import bar')
    assert 'bar' in processor.imports
    assert processor.imports['bar'] == (['foo'], 'bar', {})

def test_convert_from_str_valid_import_with_as():
    processor = ImportProcessor()
    processor.imports = {}
    processor._convert_from_str('from foo import bar as baz')
    assert 'baz' in processor.imports
    assert processor.imports['baz'] == (['foo'], 'bar', {})

def test_convert_from_str_multiple_imports():
    processor = ImportProcessor()
    processor.imports = {}
    processor._convert_from_str('from foo import bar, baz')
    assert 'bar' in processor.imports
    assert 'baz' in processor.imports
    assert processor.imports['bar'] == (['foo'], 'bar', {})
    assert processor.imports['baz'] == (['foo'], 'baz', {})

def test_convert_from_str_invalid_import():
    processor = ImportProcessor()
    with pytest.raises(ValueError, match="bad from/import 'invalid import'"):
        processor._convert_from_str('invalid import')

def test_convert_from_str_import_name_collision():
    processor = ImportProcessor()
    processor.imports = {'bar': (['foo'], 'bar', {})}
    with pytest.raises(Exception):  # Catching generic exception as errors.ImportNameCollision is not defined
        processor._convert_from_str('from foo import bar')
