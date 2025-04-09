# file lib/ansible/utils/version.py:136-145
# lines [136, 137, 138, 139, 140, 141, 142, 144, 145]
# branches ['144->exit', '144->145']

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_initialization(mocker):
    # Mock the parse method to avoid dependency on its implementation
    mocker.patch.object(SemanticVersion, 'parse', autospec=True)

    # Test initialization without vstring
    version = SemanticVersion()
    assert version.vstring is None
    assert version.major is None
    assert version.minor is None
    assert version.patch is None
    assert version.prerelease == ()
    assert version.buildmetadata == ()

    # Test initialization with vstring
    mock_vstring = "1.2.3-alpha+001"
    version = SemanticVersion(mock_vstring)
    assert version.vstring == mock_vstring
    version.parse.assert_called_once_with(version, mock_vstring)
