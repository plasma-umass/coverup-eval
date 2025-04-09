# file: pytutils/lazy/lazy_import.py:326-335
# asked: {"lines": [326, 328, 329, 330, 331, 332, 334, 335], "branches": [[328, 0], [328, 329], [329, 330], [329, 331], [331, 332], [331, 334]]}
# gained: {"lines": [326, 328, 329, 330, 331, 332, 334], "branches": [[328, 0], [328, 329], [329, 330], [329, 331], [331, 332], [331, 334]]}

import pytest
from pytutils.lazy.lazy_import import ImportProcessor

class TestImportProcessor:
    
    def setup_method(self):
        self.processor = ImportProcessor()
        self.processor.imports = {}

    def test_build_map_import(self):
        text = "import os, sys as system"
        self.processor._build_map(text)
        assert 'os' in self.processor.imports
        assert 'system' in self.processor.imports

    def test_build_map_from(self):
        text = "from os import path, environ as env"
        self.processor._build_map(text)
        assert 'path' in self.processor.imports
        assert 'env' in self.processor.imports

    def test_build_map_invalid(self):
        text = "invalid import line"
        with pytest.raises(Exception):  # Catching generic exception as errors.InvalidImportLine is not available
            self.processor._build_map(text)

    def test_canonicalize_import_text(self):
        text = "import os\nfrom sys import path"
        result = self.processor._canonicalize_import_text(text)
        assert result == ["import os", "from sys import path"]

    def test_convert_import_str(self):
        import_str = "import os, sys as system"
        self.processor._convert_import_str(import_str)
        assert 'os' in self.processor.imports
        assert 'system' in self.processor.imports

    def test_convert_import_str_invalid(self):
        import_str = "from os import path"
        with pytest.raises(ValueError):
            self.processor._convert_import_str(import_str)

    def test_convert_from_str(self):
        from_str = "from os import path, environ as env"
        self.processor._convert_from_str(from_str)
        assert 'path' in self.processor.imports
        assert 'env' in self.processor.imports

    def test_convert_from_str_invalid(self):
        from_str = "import os"
        with pytest.raises(ValueError):
            self.processor._convert_from_str(from_str)
