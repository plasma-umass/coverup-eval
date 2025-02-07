# file: dataclasses_json/mm.py:178-180
# asked: {"lines": [178, 180], "branches": []}
# gained: {"lines": [178], "branches": []}

import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_dumps():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
        schema.dumps(obj=[])
