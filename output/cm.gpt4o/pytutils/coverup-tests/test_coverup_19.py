# file pytutils/log.py:24-34
# lines [24, 34]
# branches []

import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context(mocker):
    # Mock the inspect.stack to control the call stack
    mock_stack = [
        (None, None, None, None, None, None),
        (None, None, None, None, None, None),
        (mocker.Mock(f_globals={"__name__": "test_module"}), None, None, None, None, None)
    ]
    mocker.patch('inspect.stack', return_value=mock_stack)

    # Call the function and assert the expected namespace
    namespace = _namespace_from_calling_context()
    assert namespace == "test_module"
