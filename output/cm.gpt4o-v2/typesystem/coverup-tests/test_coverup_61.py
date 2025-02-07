# file: typesystem/fields.py:305-306
# asked: {"lines": [305, 306], "branches": []}
# gained: {"lines": [305, 306], "branches": []}

import pytest
from typesystem.fields import Float

def test_float_numeric_type():
    field = Float()
    assert field.numeric_type is float
