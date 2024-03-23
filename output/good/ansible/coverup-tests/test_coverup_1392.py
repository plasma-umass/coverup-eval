# file lib/ansible/utils/vars.py:235-254
# lines [249]
# branches ['248->249']

import pytest
from ansible.utils.vars import _isidentifier_PY3
from ansible.module_utils.six import string_types
import keyword

@pytest.fixture
def cleanup():
    # No cleanup is necessary for this test as it does not modify any state
    yield
    # No cleanup code required

def test_isidentifier_non_identifier(cleanup):
    non_identifier = '123abc'
    assert not _isidentifier_PY3(non_identifier), "String that does not start with a letter or underscore should not be an identifier"
