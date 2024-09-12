# file: lib/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [140, 141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [140, 141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_parse_valid_version_with_patch():
    version = StrictVersion()
    version.parse("1.2.3")
    assert version.version == (1, 2, 3)
    assert version.prerelease is None

def test_strict_version_parse_valid_version_without_patch():
    version = StrictVersion()
    version.parse("1.2")
    assert version.version == (1, 2, 0)
    assert version.prerelease is None

def test_strict_version_parse_valid_version_with_prerelease():
    version = StrictVersion()
    version.parse("1.2.3a1")
    assert version.version == (1, 2, 3)
    assert version.prerelease == ('a', 1)

def test_strict_version_parse_invalid_version():
    version = StrictVersion()
    with pytest.raises(ValueError, match="invalid version number '1.2.3.4'"):
        version.parse("1.2.3.4")
