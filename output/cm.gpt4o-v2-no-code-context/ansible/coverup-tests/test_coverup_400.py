# file: lib/ansible/plugins/filter/mathstuff.py:169-176
# asked: {"lines": [169, 170, 171, 172, 174, 175, 176], "branches": [[171, 172], [171, 174]]}
# gained: {"lines": [169, 170, 171, 172, 174, 175, 176], "branches": [[171, 172], [171, 174]]}

import pytest
from ansible.plugins.filter.mathstuff import inversepower, AnsibleFilterTypeError

def test_inversepower_base_2():
    assert inversepower(4) == 2.0

def test_inversepower_non_base_2():
    assert inversepower(27, 3) == 3.0

def test_inversepower_value_error():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower(-1, 2)

def test_inversepower_type_error():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower("string", 2)
