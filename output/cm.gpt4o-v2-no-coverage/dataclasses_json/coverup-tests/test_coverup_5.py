# file: dataclasses_json/undefined.py:59-73
# asked: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict

# Assuming the following imports based on the provided code
from dataclasses_json.undefined import _RaiseUndefinedParameters, _UndefinedParameterAction, UndefinedParameterError

@dataclass
class DummyClass:
    defined_param: Any = field(default=None)

def test_handle_from_dict_with_only_defined_parameters():
    kvs = {'defined_param': 'value'}
    result = _RaiseUndefinedParameters.handle_from_dict(DummyClass, kvs)
    assert result == kvs

def test_handle_from_dict_with_undefined_parameters():
    kvs = {'undefined_param': 'value'}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(DummyClass, kvs)
    assert str(exc_info.value) == "Received undefined initialization arguments {'undefined_param': 'value'}"

def test_handle_from_dict_with_mixed_parameters():
    kvs = {'defined_param': 'value', 'undefined_param': 'value'}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(DummyClass, kvs)
    assert str(exc_info.value) == "Received undefined initialization arguments {'undefined_param': 'value'}"
