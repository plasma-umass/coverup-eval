# file pysnooper/tracer.py:237-244
# lines [237, 238, 239, 241, 242, 244]
# branches ['238->239', '238->241', '241->242', '241->244']

import pytest
import inspect
from unittest.mock import patch
from pysnooper.tracer import Tracer

# Assuming the DISABLED variable is a global variable in the pysnooper.tracer module
# If it's defined elsewhere, the import and patch target would need to be adjusted accordingly

@pytest.fixture
def tracer():
    return Tracer()

def test_tracer_with_disabled_flag(tracer):
    with patch('pysnooper.tracer.DISABLED', True):
        def dummy_function():
            pass

        class DummyClass:
            pass

        # Test with a function
        wrapped_function = tracer(dummy_function)
        assert wrapped_function is dummy_function, "Tracer should return the original function when disabled"

        # Test with a class
        wrapped_class = tracer(DummyClass)
        assert wrapped_class is DummyClass, "Tracer should return the original class when disabled"

def test_tracer_with_function(tracer):
    def dummy_function():
        pass

    with patch.object(tracer, '_wrap_function') as mock_wrap_function:
        mock_wrap_function.return_value = 'wrapped_function'
        wrapped_function = tracer(dummy_function)
        mock_wrap_function.assert_called_once_with(dummy_function)
        assert wrapped_function == 'wrapped_function', "Tracer should wrap the function when not disabled"

def test_tracer_with_class(tracer):
    class DummyClass:
        pass

    with patch.object(tracer, '_wrap_class') as mock_wrap_class:
        mock_wrap_class.return_value = 'wrapped_class'
        wrapped_class = tracer(DummyClass)
        mock_wrap_class.assert_called_once_with(DummyClass)
        assert wrapped_class == 'wrapped_class', "Tracer should wrap the class when not disabled"
