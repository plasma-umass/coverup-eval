# file lib/ansible/utils/version.py:128-135
# lines [128, 129, 134]
# branches []

import pytest
from ansible.utils.version import SemanticVersion
import re

SEMVER_RE = re.compile(
    r"^(?P<major>0|[1-9]\d*)\."
    r"(?P<minor>0|[1-9]\d*)\."
    r"(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>(?:0|[1-9A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+(?P<buildmetadata>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)

@pytest.fixture
def mock_semver_re(mocker):
    original_semver_re = SemanticVersion.version_re
    SemanticVersion.version_re = SEMVER_RE
    yield
    SemanticVersion.version_re = original_semver_re

def test_semantic_version(mock_semver_re):
    version_str = "1.2.3-alpha.1+build.123"
    match = SemanticVersion.version_re.match(version_str)
    assert match is not None
    assert match.group("major") == "1"
    assert match.group("minor") == "2"
    assert match.group("patch") == "3"
    assert match.group("prerelease") == "alpha.1"
    assert match.group("buildmetadata") == "build.123"
