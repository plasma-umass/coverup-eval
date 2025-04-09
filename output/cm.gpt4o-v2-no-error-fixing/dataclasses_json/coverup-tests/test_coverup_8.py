# file: dataclasses_json/undefined.py:59-73
# asked: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict

# Assuming the following imports based on the provided code
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError

@dataclass
class ExampleClass:
    defined_param: int
    another_param: str = field(default="default_value")

def test_handle_from_dict_with_known_parameters():
    kvs = {"defined_param": 42, "another_param": "test"}
    result = _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert result == kvs

def test_handle_from_dict_with_unknown_parameters():
    kvs = {"defined_param": 42, "unknown_param": "test"}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert "Received undefined initialization arguments" in str(exc_info.value)
