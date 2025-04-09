# file: lib/ansible/plugins/filter/mathstuff.py:162-166
# asked: {"lines": [162, 163, 164, 165, 166], "branches": []}
# gained: {"lines": [162, 163, 164, 165, 166], "branches": []}

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import power

def test_power_valid():
    assert power(2, 3) == 8
    assert power(4, 0.5) == 2

def test_power_invalid_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        power('two', 3)
    assert 'pow() can only be used on numbers' in str(excinfo.value)

    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        power(2, 'three')
    assert 'pow() can only be used on numbers' in str(excinfo.value)
