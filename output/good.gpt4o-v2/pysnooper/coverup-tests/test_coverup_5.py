# file: pysnooper/tracer.py:289-291
# asked: {"lines": [289, 290, 291], "branches": []}
# gained: {"lines": [289, 290, 291], "branches": []}

import pytest
from unittest.mock import MagicMock
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    tracer = Tracer()
    tracer._write = MagicMock()
    tracer.prefix = 'TEST: '
    return tracer

def test_write(tracer):
    test_string = "Hello, World!"
    tracer.write(test_string)
    expected_output = f'TEST: {test_string}\n'
    tracer._write.assert_called_once_with(expected_output)
