# file flutils/decorators.py:61-69
# lines [63]
# branches ['62->63']

import pytest
from flutils.decorators import cached_property

class TestClass:
    @cached_property
    def test_prop(self):
        return 123

@pytest.fixture
def test_instance():
    return TestClass()

def test_cached_property_get_with_none():
    # Create a dummy function to use with cached_property
    def dummy_func(self):
        return 123

    # Create a cached_property instance with the dummy function
    cached_prop = cached_property(dummy_func)
    
    # Call __get__ with obj as None to hit line 63
    result = cached_prop.__get__(None, TestClass)
    
    # Assert that the result is the cached_property instance itself
    assert result is cached_prop

def test_cached_property_get_with_obj(test_instance):
    # Ensure that the property is not yet in the instance's __dict__
    assert 'test_prop' not in test_instance.__dict__
    
    # Access the property to trigger the caching mechanism
    value = test_instance.test_prop
    
    # Check that the value is correct and that it's cached
    assert value == 123
    assert 'test_prop' in test_instance.__dict__
    assert test_instance.__dict__['test_prop'] == value
