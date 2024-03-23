# file py_backwards/utils/helpers.py:39-40
# lines [39, 40]
# branches []

import sys
from io import StringIO
import pytest
from py_backwards.utils.helpers import warn

def test_warn(capsys):
    test_message = "This is a test warning"
    warn(test_message)
    captured = capsys.readouterr()
    assert test_message in captured.err
