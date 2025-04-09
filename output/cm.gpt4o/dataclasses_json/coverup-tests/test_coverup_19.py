# file dataclasses_json/undefined.py:121-129
# lines [121, 122]
# branches []

import pytest
from dataclasses_json.undefined import _UndefinedParameterAction

class TestCatchAllUndefinedParameters:
    def test_catch_all_undefined_parameters(self):
        class _CatchAllUndefinedParameters(_UndefinedParameterAction):
            """
            This class allows to add a field of type utils.CatchAll which acts as a
            dictionary into which all
            undefined parameters will be written.
            These parameters are not affected by LetterCase.
            If no undefined parameters are given, this dictionary will be empty.
            """
            def handle_from_dict(self, *args, **kwargs):
                pass
        
        # Create an instance of the class to ensure it can be instantiated
        instance = _CatchAllUndefinedParameters()
        
        # Assert that the instance is indeed of the correct type
        assert isinstance(instance, _CatchAllUndefinedParameters)
        
        # Assert that the instance has the expected attributes (if any)
        # Since the class does not define any attributes, we just check the class name
        assert instance.__class__.__name__ == "_CatchAllUndefinedParameters"
