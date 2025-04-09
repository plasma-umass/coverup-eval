# file: flutils/pathutils.py:563-566
# asked: {"lines": [563, 564, 565, 566], "branches": []}
# gained: {"lines": [563, 564, 565, 566], "branches": []}

import pytest
import sys
import os
from pathlib import Path
from flutils.pathutils import normalize_path, _normalize_path_bytes

def test_normalize_path_bytes():
    # Test with a simple byte string
    byte_path = b'/tmp/test'
    expected_path = Path('/tmp/test')
    assert _normalize_path_bytes(byte_path) == expected_path

    # Test with a byte string containing home directory
    byte_path = b'~/tmp/test'
    expected_path = Path.home() / 'tmp/test'
    assert _normalize_path_bytes(byte_path) == expected_path

    # Test with a byte string containing environment variable
    byte_path = b'$HOME/tmp/test'
    expected_path = Path(os.path.expandvars('$HOME/tmp/test'))
    assert _normalize_path_bytes(byte_path) == expected_path

    # Test with a relative byte string
    byte_path = b'tmp/test'
    expected_path = Path(os.getcwd()) / 'tmp/test'
    assert _normalize_path_bytes(byte_path) == expected_path

    # Test with a byte string containing redundant separators and up-level references
    byte_path = b'/tmp/foo/../test'
    expected_path = Path('/tmp/test')
    assert _normalize_path_bytes(byte_path) == expected_path

    # Test with a byte string containing mixed case
    byte_path = b'/TMP/TEST'
    expected_path = Path('/TMP/TEST')
    assert _normalize_path_bytes(byte_path) == expected_path
