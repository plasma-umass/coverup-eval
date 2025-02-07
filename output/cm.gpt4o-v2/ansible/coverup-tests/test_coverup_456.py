# file: lib/ansible/plugins/filter/mathstuff.py:152-159
# asked: {"lines": [152, 153, 154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}
# gained: {"lines": [152, 153, 154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}

import pytest
import math
from ansible.errors import AnsibleFilterTypeError
from ansible.module_utils._text import to_native
from ansible.plugins.filter.mathstuff import logarithm

def test_logarithm_base_10():
    assert logarithm(100, 10) == math.log10(100)

def test_logarithm_base_e():
    assert logarithm(math.e) == math.log(math.e, math.e)

def test_logarithm_custom_base():
    assert logarithm(8, 2) == math.log(8, 2)

def test_logarithm_type_error():
    with pytest.raises(AnsibleFilterTypeError, match="log\\(\\) can only be used on numbers: "):
        logarithm("not a number", 10)
