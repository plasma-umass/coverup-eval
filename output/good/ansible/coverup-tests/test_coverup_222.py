# file lib/ansible/module_utils/compat/version.py:140-156
# lines [140, 141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156]
# branches ['142->143', '142->145', '148->149', '148->151', '153->154', '153->156']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_parsing_valid():
    version_string = "1.2.3a4"
    version = StrictVersion()
    version.parse(version_string)
    assert version.version == (1, 2, 3)
    assert version.prerelease == ('a', 4)

def test_strict_version_parsing_invalid():
    version_string = "invalid_version"
    version = StrictVersion()
    with pytest.raises(ValueError):
        version.parse(version_string)

def test_strict_version_parsing_no_patch():
    version_string = "1.2"
    version = StrictVersion()
    version.parse(version_string)
    assert version.version == (1, 2, 0)
    assert version.prerelease is None

def test_strict_version_parsing_no_prerelease():
    version_string = "1.2.3"
    version = StrictVersion()
    version.parse(version_string)
    assert version.version == (1, 2, 3)
    assert version.prerelease is None
