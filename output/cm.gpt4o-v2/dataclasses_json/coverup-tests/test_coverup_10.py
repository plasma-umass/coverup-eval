# file: dataclasses_json/mm.py:169-172
# asked: {"lines": [169, 170, 172], "branches": []}
# gained: {"lines": [169, 170], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_schemaf_dumps_list():
    data = [{"key": "value"}]

    with patch.object(SchemaF, 'dumps', return_value='[{"key": "value"}]') as mock_dumps:
        result = SchemaF.dumps(SchemaF, data, many=True)
        mock_dumps.assert_called_once_with(SchemaF, data, many=True)
        assert result == '[{"key": "value"}]'

def test_schemaf_dumps_single():
    data = {"key": "value"}

    with patch.object(SchemaF, 'dumps', return_value='{"key": "value"}') as mock_dumps:
        result = SchemaF.dumps(SchemaF, data, many=False)
        mock_dumps.assert_called_once_with(SchemaF, data, many=False)
        assert result == '{"key": "value"}'
