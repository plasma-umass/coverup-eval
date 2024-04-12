# file typesystem/formats.py:27-41
# lines [35, 38, 41]
# branches []

import pytest
from typesystem.formats import BaseFormat

class DummyFormat(BaseFormat):
    pass

@pytest.fixture
def dummy_format():
    return DummyFormat()

def test_base_format_is_native_type_not_implemented(dummy_format):
    with pytest.raises(NotImplementedError):
        dummy_format.is_native_type(None)

def test_base_format_validate_not_implemented(dummy_format):
    with pytest.raises(NotImplementedError):
        dummy_format.validate(None)

def test_base_format_serialize_not_implemented(dummy_format):
    with pytest.raises(NotImplementedError):
        dummy_format.serialize(None)
