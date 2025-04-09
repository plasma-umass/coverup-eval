# file lib/ansible/module_utils/compat/version.py:169-203
# lines [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203]
# branches ['170->171', '170->172', '172->173', '172->175', '175->178', '175->189', '178->179', '178->181', '189->190', '189->191', '191->192', '191->193', '193->194', '193->195', '195->196', '195->203', '196->197', '196->198', '198->199', '198->201']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_cmp():
    # Test comparison with string input
    v1 = StrictVersion("1.0")
    v2 = "1.0"
    assert v1._cmp(v2) == 0

    # Test comparison with non-StrictVersion input
    class DummyVersion:
        pass

    v3 = DummyVersion()
    assert v1._cmp(v3) == NotImplemented

    # Test numeric version comparison
    v4 = StrictVersion("1.0")
    v5 = StrictVersion("2.0")
    assert v4._cmp(v5) == -1
    assert v5._cmp(v4) == 1

    # Test prerelease comparison
    v6 = StrictVersion("1.0a1")
    v7 = StrictVersion("1.0")
    assert v6._cmp(v7) == -1
    assert v7._cmp(v6) == 1

    v8 = StrictVersion("1.0a1")
    v9 = StrictVersion("1.0a2")
    assert v8._cmp(v9) == -1
    assert v9._cmp(v8) == 1

    v10 = StrictVersion("1.0a1")
    v11 = StrictVersion("1.0a1")
    assert v10._cmp(v11) == 0

    # Test both have prerelease
    v12 = StrictVersion("1.0a1")
    v13 = StrictVersion("1.0b1")
    assert v12._cmp(v13) == -1
    assert v13._cmp(v12) == 1

    # Test neither has prerelease
    v14 = StrictVersion("1.0")
    v15 = StrictVersion("1.0")
    assert v14._cmp(v15) == 0

    # Test self has prerelease, other doesn't
    v16 = StrictVersion("1.0a1")
    v17 = StrictVersion("1.0")
    assert v16._cmp(v17) == -1
    assert v17._cmp(v16) == 1

    # Test self doesn't have prerelease, other does
    v18 = StrictVersion("1.0")
    v19 = StrictVersion("1.0a1")
    assert v18._cmp(v19) == 1
    assert v19._cmp(v18) == -1
