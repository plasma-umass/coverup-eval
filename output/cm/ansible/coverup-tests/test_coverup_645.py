# file lib/ansible/plugins/filter/mathstuff.py:162-166
# lines [162, 163, 164, 165, 166]
# branches []

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import power

def test_power_with_numbers():
    assert power(2, 3) == 8, "Power function did not return the expected result with numbers"

def test_power_with_invalid_type(mocker):
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        power('invalid', 'type')
    assert 'pow() can only be used on numbers' in str(excinfo.value), "Power function did not raise the expected AnsibleFilterTypeError with invalid types"
