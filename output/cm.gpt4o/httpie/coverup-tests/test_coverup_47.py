# file httpie/context.py:122-124
# lines [122, 123, 124]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Environment class is imported from httpie.context
from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_devnull_setter(environment):
    with patch.object(environment, '_devnull', create=True) as mock_devnull:
        environment.devnull = 'test_value'
        assert environment._devnull == 'test_value'
