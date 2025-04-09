# file: dataclasses_json/undefined.py:193-201
# asked: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}
# gained: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict

# Assuming the following imports are available from the dataclasses_json package
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@dataclass
class ExampleClass:
    defined_field: int
    catch_all_field: Dict[str, Any] = field(default_factory=dict)

def test_handle_to_dict_with_dict(monkeypatch):
    def mock_get_catch_all_field(obj):
        return ExampleClass.__dataclass_fields__['catch_all_field']

    monkeypatch.setattr(_CatchAllUndefinedParameters, "_get_catch_all_field", mock_get_catch_all_field)

    obj = ExampleClass(defined_field=1, catch_all_field={"extra_field": "extra_value"})
    kvs = {"defined_field": 1, "catch_all_field": {"extra_field": "extra_value"}}

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

    assert result == {"defined_field": 1, "extra_field": "extra_value"}

def test_handle_to_dict_without_dict(monkeypatch):
    def mock_get_catch_all_field(obj):
        return ExampleClass.__dataclass_fields__['catch_all_field']

    monkeypatch.setattr(_CatchAllUndefinedParameters, "_get_catch_all_field", mock_get_catch_all_field)

    obj = ExampleClass(defined_field=1, catch_all_field="not_a_dict")
    kvs = {"defined_field": 1, "catch_all_field": "not_a_dict"}

    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)

    assert result == {"defined_field": 1}
