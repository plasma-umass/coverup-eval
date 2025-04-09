# file: lib/ansible/utils/version.py:150-189
# asked: {"lines": [150, 151, 158, 159, 161, 162, 163, 164, 166, 167, 168, 169, 170, 171, 173, 174, 175, 177, 178, 181, 183, 184, 185, 186, 187], "branches": [[158, 159], [158, 161], [167, 168], [167, 175], [173, 167], [173, 174], [177, 178], [177, 181]]}
# gained: {"lines": [150, 151, 158, 159, 161, 162, 166, 167, 168, 169, 170, 171, 173, 175, 177, 178, 181, 183, 184, 185, 186, 187], "branches": [[158, 159], [158, 161], [167, 168], [167, 175], [173, 167], [177, 178], [177, 181]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion
from ansible.utils.version import SemanticVersion

def test_from_loose_version_valid():
    loose_version = LooseVersion("1.2.3")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3"

def test_from_loose_version_with_extra():
    loose_version = LooseVersion("1.2.3-alpha")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3-alpha"

def test_from_loose_version_invalid_type():
    with pytest.raises(ValueError, match="is not a LooseVersion"):
        SemanticVersion.from_loose_version("1.2.3")

def test_from_loose_version_non_integer():
    loose_version = LooseVersion("1.2.a")
    with pytest.raises(ValueError, match="Non integer values in"):
        SemanticVersion.from_loose_version(loose_version)

def test_from_loose_version_with_plus():
    loose_version = LooseVersion("1.2.3+build")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3+build"

def test_from_loose_version_with_dash():
    loose_version = LooseVersion("1.2.3-rc1")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3-rc1"

def test_from_loose_version_missing_attribute():
    class FakeLooseVersion:
        pass

    fake_version = FakeLooseVersion()
    with pytest.raises(ValueError, match="is not a LooseVersion"):
        SemanticVersion.from_loose_version(fake_version)
