# file thonny/jedi_utils.py:10-16
# lines [10, 11, 13, 14, 16]
# branches []

import pytest
from unittest import mock

def test_get_statement_of_position(mocker):
    import thonny.jedi_utils as ju
    import jedi.parser_utils

    # Mocking the node and pos
    node = mock.Mock()
    pos = mock.Mock()

    # Mocking the function in jedi.parser_utils
    if hasattr(jedi.parser_utils, 'get_statement_of_position'):
        mock_func = mocker.patch('jedi.parser_utils.get_statement_of_position', return_value="mocked_result")
    else:
        mock_func = mocker.patch('thonny.jedi_utils._copy_of_get_statement_of_position', return_value="mocked_result")

    # Call the function
    result = ju.get_statement_of_position(node, pos)

    # Assertions
    mock_func.assert_called_once_with(node, pos)
    assert result == "mocked_result"

    # Clean up
    mocker.stopall()
