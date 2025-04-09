# file lib/ansible/plugins/filter/mathstuff.py:152-159
# lines [153, 154, 155, 157, 158, 159]
# branches ['154->155', '154->157']

import pytest
import math
from ansible.plugins.filter.mathstuff import logarithm, AnsibleFilterTypeError

def test_logarithm_base_10():
    assert logarithm(100, 10) == 2

def test_logarithm_base_e():
    assert logarithm(math.e) == 1

def test_logarithm_custom_base():
    assert logarithm(8, 2) == 3

def test_logarithm_type_error():
    with pytest.raises(AnsibleFilterTypeError, match="log\(\) can only be used on numbers: must be real number, not str"):
        logarithm("not_a_number", 10)
