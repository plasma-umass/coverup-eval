# file lib/ansible/module_utils/common/validation.py:487-506
# lines [487, 497, 498, 500, 501, 502, 503, 504, 506]
# branches ['497->498', '497->500', '500->501', '500->506']

import pytest
from ansible.module_utils.common.validation import check_type_int

@pytest.fixture
def cleanup():
    # No cleanup is necessary for this test, but the fixture is here for consistency
    yield
    # Any cleanup code would go here

def test_check_type_int_with_valid_int(cleanup):
    assert check_type_int(42) == 42

def test_check_type_int_with_valid_string(cleanup):
    assert check_type_int("42") == 42

def test_check_type_int_with_invalid_string(cleanup):
    with pytest.raises(TypeError):
        check_type_int("not_an_int")

def test_check_type_int_with_invalid_type(cleanup):
    with pytest.raises(TypeError):
        check_type_int(42.0)
