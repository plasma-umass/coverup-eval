# file httpie/context.py:122-124
# lines [122, 123, 124]
# branches []

import pytest
from httpie.context import Environment

def test_devnull_setter(mocker):
    env = Environment()
    mocker.patch.object(env, '_devnull', create=True)

    mock_devnull = object()
    env.devnull = mock_devnull

    assert env._devnull is mock_devnull, "devnull setter did not set the _devnull attribute correctly"
