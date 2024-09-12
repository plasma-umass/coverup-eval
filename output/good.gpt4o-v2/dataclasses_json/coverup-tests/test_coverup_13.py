# file: dataclasses_json/undefined.py:59-73
# asked: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73], "branches": [[70, 71], [70, 73]]}

import pytest
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError, _UndefinedParameterAction

class TestRaiseUndefinedParameters:
    
    def test_handle_from_dict_with_known_parameters(self, mocker):
        class MockClass:
            pass
        
        mock_separate = mocker.patch.object(
            _UndefinedParameterAction, 
            '_separate_defined_undefined_kvs', 
            return_value=({"known_key": "known_value"}, {})
        )
        
        result = _RaiseUndefinedParameters.handle_from_dict(MockClass, {"known_key": "known_value"})
        
        mock_separate.assert_called_once_with(cls=MockClass, kvs={"known_key": "known_value"})
        assert result == {"known_key": "known_value"}
    
    def test_handle_from_dict_with_unknown_parameters(self, mocker):
        class MockClass:
            pass
        
        mock_separate = mocker.patch.object(
            _UndefinedParameterAction, 
            '_separate_defined_undefined_kvs', 
            return_value=({"known_key": "known_value"}, {"unknown_key": "unknown_value"})
        )
        
        with pytest.raises(UndefinedParameterError) as exc_info:
            _RaiseUndefinedParameters.handle_from_dict(MockClass, {"known_key": "known_value", "unknown_key": "unknown_value"})
        
        mock_separate.assert_called_once_with(cls=MockClass, kvs={"known_key": "known_value", "unknown_key": "unknown_value"})
        assert str(exc_info.value) == "Received undefined initialization arguments {'unknown_key': 'unknown_value'}"
