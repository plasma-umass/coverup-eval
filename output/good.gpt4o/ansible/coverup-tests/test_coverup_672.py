# file lib/ansible/module_utils/compat/version.py:101-139
# lines [101, 102, 137, 138]
# branches []

import re
import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_valid():
    valid_versions = [
        "0.4", "0.4.0", "0.4.1", "0.5a1", "0.5b3", "0.5", "0.9.6", "1.0", "1.0.4a3", "1.0.4b1", "1.0.4"
    ]
    for version in valid_versions:
        assert StrictVersion.version_re.match(version) is not None, f"Version {version} should be valid"

def test_strict_version_invalid():
    invalid_versions = [
        "1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4"
    ]
    for version in invalid_versions:
        assert StrictVersion.version_re.match(version) is None, f"Version {version} should be invalid"

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mocking or any other cleanup can be done here if needed
    yield
    # Cleanup code here if needed

