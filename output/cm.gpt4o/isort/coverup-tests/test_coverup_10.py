# file isort/format.py:21-29
# lines [21, 22, 23, 24, 25, 26, 27, 29]
# branches ['23->24', '23->26', '26->27', '26->29']

import pytest
from isort.format import format_simplified

def test_format_simplified():
    # Test case for 'from' import
    result = format_simplified("from os import path")
    assert result == "os.path"

    # Test case for 'import' import
    result = format_simplified("import os")
    assert result == "os"

    # Test case for already simplified import
    result = format_simplified("os.path")
    assert result == "os.path"

    # Test case for leading/trailing whitespace
    result = format_simplified("  from os import path  ")
    assert result == "os.path"

    # Test case for non-matching string
    result = format_simplified("something else")
    assert result == "something else"
