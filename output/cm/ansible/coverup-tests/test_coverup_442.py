# file lib/ansible/module_utils/common/validation.py:468-484
# lines [468, 478, 479, 481, 482, 484]
# branches ['478->479', '478->481', '481->482', '481->484']

import pytest
from ansible.module_utils.common.validation import check_type_bool
from ansible.module_utils.six import string_types

@pytest.mark.parametrize("value, expected", [
    (True, True),
    (False, False),
    ('1', True),
    ('on', True),
    (1, True),
    ('0', False),
    (0, False),
    ('n', False),
    ('f', False),
    ('false', False),
    ('true', True),
    ('y', True),
    ('t', True),
    ('yes', True),
    ('no', False),
    ('off', False),
])
def test_check_type_bool_valid(value, expected):
    assert check_type_bool(value) == expected

@pytest.mark.parametrize("value", [
    ('invalid',),
    (None,),
    ([],),
    ({},),
    (object(),),
])
def test_check_type_bool_invalid(value):
    with pytest.raises(TypeError):
        check_type_bool(value)
