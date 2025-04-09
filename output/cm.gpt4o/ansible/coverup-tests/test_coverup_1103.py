# file lib/ansible/utils/vars.py:257-270
# lines [258, 259, 261, 262, 264, 265, 267, 268, 270]
# branches ['258->259', '258->261', '261->262', '261->264', '264->265', '264->267', '267->268', '267->270']

import pytest
import keyword
from ansible.utils.vars import _isidentifier_PY2
from ansible.module_utils.six import string_types
from ansible.constants import INVALID_VARIABLE_NAMES

class MockConstants:
    INVALID_VARIABLE_NAMES = INVALID_VARIABLE_NAMES

ADDITIONAL_PY2_KEYWORDS = {'print'}

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.utils.vars.C', new=MockConstants)
    mocker.patch('ansible.utils.vars.ADDITIONAL_PY2_KEYWORDS', new=ADDITIONAL_PY2_KEYWORDS)

def test_isidentifier_PY2(mock_constants):
    # Test for non-string input
    assert not _isidentifier_PY2(123)

    # Test for empty string
    assert not _isidentifier_PY2('')

    # Test for invalid variable names
    assert not _isidentifier_PY2('invalid-variable-name')

    # Test for Python keyword
    assert not _isidentifier_PY2('for')

    # Test for additional Python 2 keywords
    assert not _isidentifier_PY2('print')

    # Test for valid identifier
    assert _isidentifier_PY2('valid_identifier')

    # Test for valid identifier with numbers
    assert _isidentifier_PY2('valid_identifier_123')
