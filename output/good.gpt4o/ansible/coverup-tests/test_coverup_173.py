# file lib/ansible/module_utils/compat/version.py:330-341
# lines [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341]
# branches ['331->332', '331->333', '333->334', '333->336', '336->337', '336->338', '338->339', '338->340', '340->exit', '340->341']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_cmp():
    lv1 = LooseVersion("1.0")
    lv2 = LooseVersion("1.0")
    lv3 = LooseVersion("2.0")
    lv4 = "2.0"
    lv5 = 2.0

    # Test equality
    assert lv1._cmp(lv2) == 0

    # Test less than
    assert lv1._cmp(lv3) == -1

    # Test greater than
    assert lv3._cmp(lv1) == 1

    # Test comparison with string
    assert lv1._cmp(lv4) == -1

    # Test comparison with unsupported type
    assert lv1._cmp(lv5) == NotImplemented
