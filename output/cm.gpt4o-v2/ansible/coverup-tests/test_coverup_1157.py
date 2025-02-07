# file: lib/ansible/utils/vars.py:257-270
# asked: {"lines": [258, 259, 261, 262, 264, 265, 267, 268, 270], "branches": [[258, 259], [258, 261], [261, 262], [261, 264], [264, 265], [264, 267], [267, 268], [267, 270]]}
# gained: {"lines": [258, 259, 261, 262, 264, 265, 267, 268, 270], "branches": [[258, 259], [258, 261], [261, 262], [261, 264], [264, 265], [264, 267], [267, 268], [267, 270]]}

import pytest
import keyword
from ansible import constants as C
from ansible.module_utils.six import string_types
from ansible.utils.vars import _isidentifier_PY2

ADDITIONAL_PY2_KEYWORDS = frozenset(('True', 'False', 'None'))

def test_isidentifier_py2_non_string():
    assert not _isidentifier_PY2(123)  # Non-string input

def test_isidentifier_py2_empty_string():
    assert not _isidentifier_PY2('')  # Empty string input

def test_isidentifier_py2_invalid_variable_name():
    assert not _isidentifier_PY2('1invalid')  # Invalid variable name starting with a digit
    assert not _isidentifier_PY2('invalid-variable')  # Invalid variable name with a hyphen

def test_isidentifier_py2_keyword():
    assert not _isidentifier_PY2('for')  # Python keyword
    assert not _isidentifier_PY2('True')  # Additional PY2 keyword

def test_isidentifier_py2_valid_identifier():
    assert _isidentifier_PY2('valid_variable')  # Valid identifier
    assert _isidentifier_PY2('validVariable123')  # Valid identifier with numbers

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Code to cleanup after tests run
