# file lib/ansible/module_utils/compat/version.py:330-341
# lines [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341]
# branches ['331->332', '331->333', '333->334', '333->336', '336->337', '336->338', '338->339', '338->340', '340->exit', '340->341']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_comparison():
    v1 = LooseVersion("1.0")
    v2 = LooseVersion("2.0")
    v3 = "1.0"
    v4 = "2.0"
    v5 = 1  # Non-comparable type

    # Test equality
    assert v1._cmp(v1) == 0
    assert v1._cmp(v3) == 0

    # Test less than
    assert v1._cmp(v2) == -1
    assert v1._cmp(v4) == -1

    # Test greater than
    assert v2._cmp(v1) == 1
    assert v2._cmp(v3) == 1

    # Test NotImplemented
    assert v1._cmp(v5) == NotImplemented
