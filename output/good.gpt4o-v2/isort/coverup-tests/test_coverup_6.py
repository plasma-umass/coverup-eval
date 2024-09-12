# file: isort/format.py:21-29
# asked: {"lines": [21, 22, 23, 24, 25, 26, 27, 29], "branches": [[23, 24], [23, 26], [26, 27], [26, 29]]}
# gained: {"lines": [21, 22, 23, 24, 25, 26, 27, 29], "branches": [[23, 24], [23, 26], [26, 27], [26, 29]]}

import pytest
from isort.format import format_simplified

def test_format_simplified_from_import():
    result = format_simplified("from os import path")
    assert result == "os.path"

def test_format_simplified_import():
    result = format_simplified("import os")
    assert result == "os"

def test_format_simplified_no_change():
    result = format_simplified("os.path")
    assert result == "os.path"
