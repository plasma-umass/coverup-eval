# file pytutils/log.py:24-34
# lines [24, 34]
# branches []

import pytest
from unittest.mock import patch
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context():
    with patch('pytutils.log.inspect.stack') as mock_stack:
        # Mock the stack to simulate the calling context
        mock_frame = patch('inspect.FrameInfo', create=True)
        mock_frame.f_globals = {"__name__": "mock_module"}
        mock_stack.return_value = [None, None, (mock_frame, None, None, None, None, None)]

        # Call the function and assert the result
        namespace = _namespace_from_calling_context()
        assert namespace == "mock_module"

        # Ensure that the stack was called as expected
        mock_stack.assert_called_once()

# Clean up is handled by the patch context manager, no further action required.
