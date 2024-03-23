# file lib/ansible/constants.py:33-40
# lines [33, 35, 36, 37, 38, 39, 40]
# branches []

import pytest
from ansible.constants import _deprecated
from ansible.utils.display import Display
from io import StringIO
import sys

def test_deprecated_with_display(mocker):
    # Mock Display class and its deprecated method
    mock_display = mocker.patch.object(Display, 'deprecated')

    # Call the _deprecated function which should use Display.deprecated
    _deprecated("deprecated feature", "2.10")

    # Assert that Display.deprecated was called
    mock_display.assert_called_once_with("deprecated feature", version="2.10")

def test_deprecated_with_exception(mocker):
    # Mock Display import to raise an ImportError
    mocker.patch.dict('sys.modules', {'ansible.utils.display': None})

    # Redirect stderr to capture the output
    captured_stderr = StringIO()
    mocker.patch.object(sys, 'stderr', new=captured_stderr)

    # Call the _deprecated function which should fall back to stderr
    _deprecated("deprecated feature", "2.10")

    # Assert that the correct message was written to stderr
    assert captured_stderr.getvalue() == ' [DEPRECATED] deprecated feature, to be removed in 2.10\n'

    # Clean up by resetting stderr
    sys.stderr = sys.__stderr__
