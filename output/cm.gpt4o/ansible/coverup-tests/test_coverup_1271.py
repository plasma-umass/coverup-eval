# file lib/ansible/utils/version.py:191-204
# lines [194]
# branches ['193->194']

import pytest
from ansible.utils.version import SemanticVersion

def test_invalid_semantic_version():
    invalid_version = "1.0"
    with pytest.raises(ValueError, match=f"invalid semantic version '{invalid_version}'"):
        SemanticVersion(invalid_version)
