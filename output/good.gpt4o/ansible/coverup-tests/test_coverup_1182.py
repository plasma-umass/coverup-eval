# file lib/ansible/plugins/filter/mathstuff.py:169-176
# lines [170, 171, 172, 174, 175, 176]
# branches ['171->172', '171->174']

import pytest
from ansible.plugins.filter.mathstuff import inversepower, AnsibleFilterTypeError
from ansible.module_utils._text import to_native

def test_inversepower_base_2():
    assert inversepower(4) == 2.0
    assert inversepower(9) == 3.0

def test_inversepower_other_base():
    assert inversepower(27, 3) == 3.0
    assert inversepower(16, 4) == 2.0

def test_inversepower_value_error():
    with pytest.raises(AnsibleFilterTypeError, match="root\(\) can only be used on numbers: math domain error"):
        inversepower(-1)

def test_inversepower_type_error():
    with pytest.raises(AnsibleFilterTypeError, match="root\(\) can only be used on numbers: must be real number, not str"):
        inversepower("string")
