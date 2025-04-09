# file: dataclasses_json/undefined.py:59-73
# asked: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}

import pytest
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError, _UndefinedParameterAction

def test_raise_undefined_parameters_handle_from_dict_known(monkeypatch):
    class MockClass:
        __annotations__ = {'a': int, 'b': str}

    def mock_separate_defined_undefined_kvs(cls, kvs):
        return {'a': 1, 'b': 'test'}, {}

    monkeypatch.setattr(_UndefinedParameterAction, '_separate_defined_undefined_kvs', mock_separate_defined_undefined_kvs)

    result = _RaiseUndefinedParameters.handle_from_dict(MockClass, {'a': 1, 'b': 'test'})
    assert result == {'a': 1, 'b': 'test'}

def test_raise_undefined_parameters_handle_from_dict_unknown(monkeypatch):
    class MockClass:
        __annotations__ = {'a': int, 'b': str}

    def mock_separate_defined_undefined_kvs(cls, kvs):
        return {'a': 1, 'b': 'test'}, {'c': 2}

    monkeypatch.setattr(_UndefinedParameterAction, '_separate_defined_undefined_kvs', mock_separate_defined_undefined_kvs)

    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(MockClass, {'a': 1, 'b': 'test', 'c': 2})
    assert "Received undefined initialization arguments {'c': 2}" in str(excinfo.value)
