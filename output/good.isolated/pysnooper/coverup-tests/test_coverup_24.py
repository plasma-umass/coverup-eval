# file pysnooper/tracer.py:293-307
# lines [295]
# branches ['294->295']

import pytest
import pysnooper.tracer
from unittest.mock import patch

@pytest.fixture
def disable_tracer():
    with patch.object(pysnooper.tracer, 'DISABLED', True):
        yield

def test_tracer_enter_with_disabled_tracer(disable_tracer):
    tracer = pysnooper.tracer.Tracer()
    with tracer as result:
        assert result is None
