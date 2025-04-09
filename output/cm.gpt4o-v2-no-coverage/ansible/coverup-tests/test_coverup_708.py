# file: lib/ansible/plugins/filter/mathstuff.py:162-166
# asked: {"lines": [162, 163, 164, 165, 166], "branches": []}
# gained: {"lines": [162, 163, 164, 165, 166], "branches": []}

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import power

def test_power_success():
    assert power(2, 3) == 8.0
    assert power(4, 0.5) == 2.0

def test_power_type_error():
    with pytest.raises(AnsibleFilterTypeError, match=r"pow\(\) can only be used on numbers: must be real number, not str"):
        power("two", 3)
    with pytest.raises(AnsibleFilterTypeError, match=r"pow\(\) can only be used on numbers: must be real number, not str"):
        power(2, "three")
