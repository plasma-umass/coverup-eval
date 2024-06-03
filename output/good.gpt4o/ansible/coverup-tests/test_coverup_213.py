# file lib/ansible/utils/vars.py:235-254
# lines [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254]
# branches ['236->237', '236->241', '248->249', '248->251', '251->252', '251->254']

import pytest
import keyword
from ansible.utils.vars import _isidentifier_PY3

def test_isidentifier_py3(mocker):
    # Test with a non-string type
    assert not _isidentifier_PY3(123)

    # Test with a string containing non-ascii characters
    assert not _isidentifier_PY3('identé')

    # Test with a string that is not a valid identifier
    assert not _isidentifier_PY3('123abc')

    # Test with a string that is a keyword
    assert not _isidentifier_PY3('for')

    # Test with a valid identifier
    assert _isidentifier_PY3('valid_identifier')

    # Test with a string that is a valid identifier but a keyword in another language
    mocker.patch('keyword.iskeyword', return_value=False)
    assert _isidentifier_PY3('non_keyword')

    # Clean up mock
    mocker.stopall()
