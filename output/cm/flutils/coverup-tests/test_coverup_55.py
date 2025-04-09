# file flutils/txtutils.py:233-237
# lines [237]
# branches ['236->237']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_subsequent_indent_deletion(mocker):
    # Create an instance of AnsiTextWrapper
    wrapper = AnsiTextWrapper()

    # Mock the __dict__ to include 'subsequent_indent_len'
    mocker.patch.object(wrapper, '__dict__', {'subsequent_indent_len': 10})

    # Assert 'subsequent_indent_len' is in the dictionary before setting subsequent_indent
    assert 'subsequent_indent_len' in wrapper.__dict__

    # Set subsequent_indent to trigger the deletion of 'subsequent_indent_len'
    wrapper.subsequent_indent = '  '

    # Assert 'subsequent_indent_len' is not in the dictionary after setting subsequent_indent
    assert 'subsequent_indent_len' not in wrapper.__dict__
