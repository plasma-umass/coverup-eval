# file thefuck/shells/generic.py:103-111
# lines [103, 106, 107, 109, 111]
# branches ['106->107', '106->109']

import pytest
import six
from unittest import mock
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_quote_py2(mocker, generic):
    if six.PY2:
        mock_quote = mocker.patch('pipes.quote', return_value='mocked_quote')
        result = generic.quote('test')
        mock_quote.assert_called_once_with('test')
        assert result == 'mocked_quote'

def test_quote_py3(mocker, generic):
    if not six.PY2:
        mock_quote = mocker.patch('shlex.quote', return_value='mocked_quote')
        result = generic.quote('test')
        mock_quote.assert_called_once_with('test')
        assert result == 'mocked_quote'
