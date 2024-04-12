# file isort/format.py:21-29
# lines [21, 22, 23, 24, 25, 26, 27, 29]
# branches ['23->24', '23->26', '26->27', '26->29']

import pytest
from isort.format import format_simplified

def test_format_simplified_from_import():
    # Test the branch where the import line starts with "from "
    input_line = "from module import function"
    expected_output = "module.function"
    assert format_simplified(input_line) == expected_output

def test_format_simplified_import():
    # Test the branch where the import line starts with "import "
    input_line = "import module"
    expected_output = "module"
    assert format_simplified(input_line) == expected_output

def test_format_simplified_no_prefix():
    # Test the branch where the import line does not start with "from " or "import "
    input_line = "module.function"
    expected_output = "module.function"
    assert format_simplified(input_line) == expected_output
