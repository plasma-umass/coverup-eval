# file lib/ansible/plugins/filter/mathstuff.py:169-176
# lines [169, 170, 171, 172, 174, 175, 176]
# branches ['171->172', '171->174']

import pytest
import math
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import inversepower

def test_inversepower_with_base_2():
    assert inversepower(4) == math.sqrt(4)

def test_inversepower_with_base_3():
    assert inversepower(8, base=3) == math.pow(8, 1.0 / 3)

def test_inversepower_with_invalid_base_type(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.to_native', side_effect=lambda x: str(x))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        inversepower(8, base='invalid')
    assert 'can only be used on numbers' in str(excinfo.value)

def test_inversepower_with_negative_number(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.to_native', side_effect=lambda x: str(x))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        inversepower(-8, base=2)
    assert 'can only be used on numbers' in str(excinfo.value)

def test_inversepower_with_invalid_number_type(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.to_native', side_effect=lambda x: str(x))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        inversepower('invalid', base=2)
    assert 'can only be used on numbers' in str(excinfo.value)
