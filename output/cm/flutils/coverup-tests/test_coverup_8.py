# file flutils/txtutils.py:255-259
# lines [255, 256, 257, 258, 259]
# branches ['257->258', '257->259']

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

def test_AnsiTextWrapper_placeholder_len_with_non_stripped_placeholder(mocker):
    # Mock len_without_ansi to control its return value and ensure it's called
    mock_len_without_ansi = mocker.patch('flutils.txtutils.len_without_ansi', return_value=10)

    # Create an instance of AnsiTextWrapper with a placeholder that has non-whitespace characters
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = ' \x1b[31mHello\x1b[0m '

    # Assert that placeholder_len returns the mocked length of the placeholder without ANSI codes
    assert wrapper.placeholder_len == 10
    mock_len_without_ansi.assert_called_once_with(wrapper.placeholder)

def test_AnsiTextWrapper_placeholder_len_with_stripped_placeholder():
    # Create an instance of AnsiTextWrapper with a placeholder that only has whitespace characters
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = '   '

    # Assert that placeholder_len returns 0 for a placeholder that is only whitespace
    assert wrapper.placeholder_len == 0
