# file pymonet/box.py:81-90
# lines [88, 90]
# branches []

import pytest
from pymonet.box import Box

def test_box_to_lazy_executes_missing_lines(mocker):
    # Mock the import of Lazy to ensure it's called
    lazy_module_mock = mocker.patch('pymonet.lazy.Lazy')

    # Create a Box instance with some value
    box = Box(42)

    # Call the to_lazy method which should execute the missing lines
    lazy_instance = box.to_lazy()

    # Assert that Lazy was called with the correct lambda function
    lazy_module_mock.assert_called_once()
    assert callable(lazy_module_mock.call_args[0][0])

    # Assert that the lambda function returns the correct value
    assert lazy_module_mock.call_args[0][0]() == 42
