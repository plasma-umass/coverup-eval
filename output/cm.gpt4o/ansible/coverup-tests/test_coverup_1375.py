# file lib/ansible/utils/version.py:150-189
# lines [158, 159, 161, 162, 163, 164, 166, 167, 168, 169, 170, 171, 173, 174, 175, 177, 178, 181, 183, 184, 185, 186, 187]
# branches ['158->159', '158->161', '167->168', '167->175', '173->167', '173->174', '177->178', '177->181']

import pytest
from distutils.version import LooseVersion
from ansible.utils.version import SemanticVersion

def test_semantic_version_from_loose_version(mocker):
    # Mock the LooseVersion class to ensure isinstance checks pass
    mocker.patch('ansible.utils.version.LooseVersion', LooseVersion)

    # Test with a valid LooseVersion
    loose_version = LooseVersion("1.2.3")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3"

    # Test with a LooseVersion that has a pre-release
    loose_version = LooseVersion("1.2.3-alpha")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3-alpha"

    # Test with a LooseVersion that has build metadata
    loose_version = LooseVersion("1.2.3+build")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3+build"

    # Test with a LooseVersion that has both pre-release and build metadata
    loose_version = LooseVersion("1.2.3-alpha+build")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.3-alpha+build"

    # Test with a LooseVersion that has fewer than 3 components
    loose_version = LooseVersion("1.2")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == "1.2.0"

    # Test with a LooseVersion that has non-integer values
    loose_version = LooseVersion("1.2.a")
    with pytest.raises(ValueError, match="Non integer values in"):
        SemanticVersion.from_loose_version(loose_version)

    # Test with an invalid LooseVersion type
    with pytest.raises(ValueError, match="is not a LooseVersion"):
        SemanticVersion.from_loose_version("1.2.3")

    # Test with a LooseVersion that raises AttributeError
    class InvalidLooseVersion:
        pass

    invalid_loose_version = InvalidLooseVersion()
    with pytest.raises(ValueError, match="is not a LooseVersion"):
        SemanticVersion.from_loose_version(invalid_loose_version)
