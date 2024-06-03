# file lib/ansible/module_utils/splitter.py:215-219
# lines [217, 218, 219]
# branches ['217->218', '217->219']

import pytest
from ansible.module_utils.splitter import unquote

def test_unquote(mocker):
    # Mock the is_quoted function to control its return value
    mock_is_quoted = mocker.patch('ansible.module_utils.splitter.is_quoted')

    # Test case where is_quoted returns True
    mock_is_quoted.return_value = True
    assert unquote('"quoted"') == 'quoted'
    assert unquote("'quoted'") == 'quoted'

    # Test case where is_quoted returns False
    mock_is_quoted.return_value = False
    assert unquote('not quoted') == 'not quoted'
    assert unquote('') == ''
