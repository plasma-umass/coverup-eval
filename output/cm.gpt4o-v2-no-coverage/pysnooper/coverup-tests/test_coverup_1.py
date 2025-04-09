# file: pysnooper/tracer.py:289-291
# asked: {"lines": [289, 290, 291], "branches": []}
# gained: {"lines": [289, 290, 291], "branches": []}

import pytest
from unittest.mock import MagicMock
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    return Tracer()

def test_write(tracer):
    mock_write = MagicMock()
    tracer._write = mock_write
    tracer.prefix = "TEST: "
    
    tracer.write("Hello, World!")
    
    mock_write.assert_called_once_with("TEST: Hello, World!\n")
