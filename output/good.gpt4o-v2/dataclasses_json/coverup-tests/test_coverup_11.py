# file: dataclasses_json/mm.py:174-176
# asked: {"lines": [174, 175, 176], "branches": []}
# gained: {"lines": [174, 175], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

@pytest.fixture
def schemaf_instance():
    with patch.object(SchemaF, '__init__', lambda self: None):
        yield SchemaF()

def test_schemaf_dumps_overload(schemaf_instance):
    with patch.object(SchemaF, 'dumps', return_value="{}") as mock_dumps:
        result = schemaf_instance.dumps(obj=[], many=True)
        mock_dumps.assert_called_once_with(obj=[], many=True)
        assert result == "{}"

    with patch.object(SchemaF, 'dumps', return_value="{}") as mock_dumps:
        result = schemaf_instance.dumps(obj={}, many=False)
        mock_dumps.assert_called_once_with(obj={}, many=False)
        assert result == "{}"
