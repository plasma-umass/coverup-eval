# file: flutils/txtutils.py:255-259
# asked: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}
# gained: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch, PropertyMock

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_placeholder_len_empty_placeholder(ansi_text_wrapper):
    with patch.object(AnsiTextWrapper, 'placeholder', new_callable=PropertyMock) as mock_placeholder:
        mock_placeholder.return_value = '   '
        assert ansi_text_wrapper.placeholder_len == 0

def test_placeholder_len_non_empty_placeholder(ansi_text_wrapper):
    with patch.object(AnsiTextWrapper, 'placeholder', new_callable=PropertyMock) as mock_placeholder:
        mock_placeholder.return_value = '\x1b[31mtest\x1b[0m'
        assert ansi_text_wrapper.placeholder_len == 4  # Assuming len_without_ansi removes ANSI codes and returns length of 'test'
