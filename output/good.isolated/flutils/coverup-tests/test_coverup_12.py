# file flutils/txtutils.py:223-227
# lines [223, 224, 225, 226, 227]
# branches ['225->226', '225->227']

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

# Assuming len_without_ansi is a function in the same module that needs to be tested
# If it's from another module, the import should be adjusted accordingly

def test_initial_indent_len_with_ansi_codes():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = "\x1b[31mHello\x1b[0m"

    with patch('flutils.txtutils.len_without_ansi') as mock_len_without_ansi:
        mock_len_without_ansi.return_value = 5
        assert wrapper.initial_indent_len == 5
        mock_len_without_ansi.assert_called_once_with("\x1b[31mHello\x1b[0m")

def test_initial_indent_len_without_initial_indent():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = ""
    assert wrapper.initial_indent_len == 0

# Run the tests
pytest.main()
