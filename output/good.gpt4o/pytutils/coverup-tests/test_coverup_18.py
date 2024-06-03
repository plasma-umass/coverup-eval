# file pytutils/lazy/simple_import.py:14-21
# lines [14, 15, 18, 20, 21]
# branches []

import pytest
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_class():
    # Create an instance of NonLocal with a specific value
    nonlocal_instance = NonLocal(value=10)
    
    # Assert that the value is correctly set
    assert nonlocal_instance.value == 10
    
    # Change the value and assert the change
    nonlocal_instance.value = 20
    assert nonlocal_instance.value == 20

    # Clean up by deleting the instance
    del nonlocal_instance

# Mocking the NonLocal class to ensure it is tested in isolation
@pytest.fixture
def mock_nonlocal_class(mocker):
    mocker.patch('pytutils.lazy.simple_import.NonLocal', NonLocal)

def test_nonlocal_class_with_mock(mock_nonlocal_class):
    # Create an instance of NonLocal with a specific value
    nonlocal_instance = NonLocal(value=30)
    
    # Assert that the value is correctly set
    assert nonlocal_instance.value == 30
    
    # Change the value and assert the change
    nonlocal_instance.value = 40
    assert nonlocal_instance.value == 40

    # Clean up by deleting the instance
    del nonlocal_instance
