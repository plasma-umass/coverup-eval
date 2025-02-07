# file: dataclasses_json/mm.py:146-153
# asked: {"lines": [146, 152, 153], "branches": []}
# gained: {"lines": [146, 152, 153], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_init_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        SchemaF()
