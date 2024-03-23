# file lib/ansible/plugins/filter/mathstuff.py:152-159
# lines [152, 153, 154, 155, 157, 158, 159]
# branches ['154->155', '154->157']

import math
import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import logarithm

def test_logarithm_with_base_e():
    assert logarithm(1) == 0
    assert logarithm(math.e) == 1

def test_logarithm_with_base_10():
    assert logarithm(1, 10) == 0
    assert logarithm(10, 10) == 1

def test_logarithm_with_different_base():
    assert logarithm(1, 2) == 0
    assert logarithm(8, 2) == 3

def test_logarithm_with_invalid_type():
    with pytest.raises(AnsibleFilterTypeError):
        logarithm('invalid')

def test_logarithm_with_zero():
    with pytest.raises(ValueError):
        logarithm(0, 10)
