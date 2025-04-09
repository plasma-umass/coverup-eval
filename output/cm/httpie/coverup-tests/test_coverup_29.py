# file httpie/context.py:116-120
# lines [116, 117, 118, 119, 120]
# branches ['118->119', '118->120']

import os
import pytest
from httpie.context import Environment

@pytest.fixture
def environment():
    env = Environment()
    yield env
    # Cleanup
    if env._devnull is not None:
        env._devnull.close()
        env._devnull = None

def test_devnull_property(mocker, environment):
    # Mock os.devnull to avoid using the actual OS device
    mocker.patch('os.devnull', new_callable=mocker.PropertyMock(return_value='/dev/null'))
    
    # Access the property twice to test both branches (None and not None)
    devnull_first_access = environment.devnull
    devnull_second_access = environment.devnull
    
    # Verify that the file was opened correctly
    assert not devnull_first_access.closed
    assert devnull_first_access.mode == 'w+'
    
    # Verify that the second access returns the same file object
    assert devnull_first_access is devnull_second_access
