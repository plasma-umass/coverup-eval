# file lib/ansible/module_utils/compat/version.py:169-203
# lines [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203]
# branches ['170->171', '170->172', '172->173', '172->175', '175->178', '175->189', '178->179', '178->181', '189->190', '189->191', '191->192', '191->193', '193->194', '193->195', '195->196', '195->203', '196->197', '196->198', '198->199', '198->201']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_comparison():
    # Case 1: neither has prerelease; they're equal
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == 0

    # Case 2: self has prerelease, other doesn't; other is greater
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == -1

    # Case 3: self doesn't have prerelease, other does: self is greater
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 1

    # Case 4: both have prerelease: must compare them!
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    assert v1._cmp(v2) == -1

    v1 = StrictVersion("1.0a2")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 1

    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 0

    # Test comparison with a string that should be converted to StrictVersion
    assert v1._cmp("1.0") == -1

    # Test comparison with an unsupported type
    assert v1._cmp(1.0) == NotImplemented
