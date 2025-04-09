# file pytutils/lazy/lazy_regex.py:153-162
# lines [153, 158, 159, 162]
# branches ['158->159', '158->162']

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    def test_getattr_missing_attribute(self, mocker):
        # Mock the _compile_and_collapse method to avoid actual regex compilation
        mocker.patch.object(LazyRegex, '_compile_and_collapse')
        
        # Create a LazyRegex instance
        lazy_regex = LazyRegex()
        
        # Set the _real_regex attribute to None to simulate uninitialized state
        lazy_regex._real_regex = None
        
        # Access a non-existent attribute to trigger the __getattr__ method
        with pytest.raises(AttributeError):
            _ = lazy_regex.non_existent_attribute
        
        # Assert that _compile_and_collapse was called
        assert LazyRegex._compile_and_collapse.called
        
        # Clean up by unpatching the method
        mocker.stopall()
