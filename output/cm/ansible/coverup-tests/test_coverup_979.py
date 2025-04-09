# file lib/ansible/modules/apt_repository.py:189-190
# lines [189, 190]
# branches []

import pytest
from ansible.modules.apt_repository import InvalidSource

def test_invalid_source_exception():
    with pytest.raises(InvalidSource) as exc_info:
        raise InvalidSource("Invalid repository source")

    assert str(exc_info.value) == "Invalid repository source", "InvalidSource exception message does not match"
