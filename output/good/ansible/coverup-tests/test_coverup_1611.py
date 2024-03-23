# file lib/ansible/module_utils/compat/version.py:169-203
# lines [178, 179, 181, 203]
# branches ['175->178', '178->179', '178->181', '195->203']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_comparison():
    # Test numeric version comparison
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1._cmp(v2) == -1, "v1 should be less than v2"
    assert v2._cmp(v1) == 1, "v2 should be greater than v1"

    # Test the AssertionError line
    # This test is removed because the AssertionError cannot be reached
    # through normal use of the StrictVersion class.

def test_strict_version_comparison_with_str():
    # Test comparison with string input
    v1 = StrictVersion("1.0")
    assert v1._cmp("2.0") == -1, "v1 should be less than '2.0'"
    assert v1._cmp("0.9") == 1, "v1 should be greater than '0.9'"

def test_strict_version_not_implemented():
    v1 = StrictVersion("1.0")
    assert v1._cmp(object()) == NotImplemented, "Comparison with non-StrictVersion should return NotImplemented"

# The following code is not part of the test and should not be executed
# directly as per the instructions. It is only here for completeness.
# if __name__ == "__main__":
#     pytest.main()
