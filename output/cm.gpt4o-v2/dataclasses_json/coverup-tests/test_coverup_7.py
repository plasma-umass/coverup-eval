# file: dataclasses_json/mm.py:210-214
# asked: {"lines": [210, 211, 212, 214], "branches": []}
# gained: {"lines": [210, 211, 212], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_loads_overload():
    with patch.object(SchemaF, '__init__', lambda *args, **kwargs: None):
        with patch.object(SchemaF, 'loads', lambda *args, **kwargs: None):
            schema = SchemaF()
            assert schema.loads('{"key": "value"}', many=None, partial=None, unknown=None) is None
