# file: typesystem/formats.py:27-41
# asked: {"lines": [35, 38, 41], "branches": []}
# gained: {"lines": [35, 38, 41], "branches": []}

import pytest
from typesystem.formats import BaseFormat
from typesystem.base import ValidationError

class TestBaseFormat:
    
    def test_is_native_type_not_implemented(self):
        base_format = BaseFormat()
        with pytest.raises(NotImplementedError):
            base_format.is_native_type("test")
    
    def test_validate_not_implemented(self):
        base_format = BaseFormat()
        with pytest.raises(NotImplementedError):
            base_format.validate("test")
    
    def test_serialize_not_implemented(self):
        base_format = BaseFormat()
        with pytest.raises(NotImplementedError):
            base_format.serialize("test")
