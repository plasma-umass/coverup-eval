# file lib/ansible/plugins/filter/mathstuff.py:162-166
# lines [162, 163, 164, 165, 166]
# branches []

import pytest
import math
from ansible.plugins.filter.mathstuff import power
from ansible.errors import AnsibleFilterTypeError
from ansible.module_utils._text import to_native

def test_power():
    # Test normal case
    assert power(2, 3) == 8.0

    # Test with float
    assert power(2.0, 3) == 8.0

    # Test with negative exponent
    assert power(2, -3) == 0.125

    # Test with zero exponent
    assert power(2, 0) == 1.0

    # Test with invalid type
    with pytest.raises(AnsibleFilterTypeError, match=r"pow\(\) can only be used on numbers: must be real number, not str"):
        power('a', 3)
