# file flutils/txtutils.py:273-396
# lines [348, 378, 380, 382, 387, 388, 391, 392, 393]
# branches ['342->293', '356->378', '378->380', '378->393', '387->391', '387->393']

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

def test_ansi_text_wrapper_full_coverage(mocker):
    # Mock the len_without_ansi function to control its behavior
    mock_len_without_ansi = mocker.patch('flutils.txtutils.len_without_ansi', side_effect=lambda x: len(x))

    # Define a string that will trigger the uncovered lines
    long_word = 'a' * 50
    text = f"{long_word} {long_word} {long_word}"

    # Create an instance of AnsiTextWrapper with specific settings to cover the lines
    wrapper = AnsiTextWrapper(width=10, max_lines=2, placeholder='...')

    # Call the wrap method which internally calls _wrap_chunks
    wrapped_text = wrapper.wrap(text)

    # Check the postconditions
    assert wrapped_text == [long_word[:10], '...'], "Wrapped text does not match expected output"

    # Verify that len_without_ansi was called with the expected arguments
    assert mock_len_without_ansi.call_count > 0, "len_without_ansi was not called"

    # Clean up the mock
    mocker.stopall()
