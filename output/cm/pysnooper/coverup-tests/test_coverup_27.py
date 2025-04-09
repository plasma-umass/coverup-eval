# file pysnooper/tracer.py:206-235
# lines [229, 230]
# branches ['228->230']

import pytest
from pysnooper.tracer import Tracer
from pysnooper import pycompat

@pytest.fixture
def cleanup():
    # Fixture to clean up any global state after the test
    yield
    # No global state to clean up in this case

def test_custom_repr_non_iterable(mocker, cleanup):
    # Mock the isinstance function to force the condition to be True
    mocker.patch('pysnooper.tracer.isinstance', side_effect=lambda x, y: False)
    
    # Create a Tracer instance with a custom_repr that should trigger the condition
    custom_repr = (lambda x: 'representation', 'not_iterable')
    tracer = Tracer(custom_repr=custom_repr)
    
    # Assert that the custom_repr was turned into a tuple of tuples
    assert isinstance(tracer.custom_repr, tuple)
    assert isinstance(tracer.custom_repr[0], tuple)
    assert tracer.custom_repr[0][0] == custom_repr[0]
    assert tracer.custom_repr[0][1] == custom_repr[1]
