# file dataclasses_json/undefined.py:59-73
# lines [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73]
# branches ['70->71', '70->73']

import pytest
from dataclasses_json.undefined import UndefinedParameterError, _RaiseUndefinedParameters
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict, Any

@dataclass_json
@dataclass
class Example:
    a: int
    b: str

def test_raise_undefined_parameters_handle_from_dict():
    with pytest.raises(UndefinedParameterError) as exc_info:
        _RaiseUndefinedParameters.handle_from_dict(Example, {'a': 1, 'b': 'test', 'c': 2.0})
    assert "Received undefined initialization arguments {'c': 2.0}" in str(exc_info.value)
