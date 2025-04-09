# file: lib/ansible/modules/apt_repository.py:189-190
# asked: {"lines": [189, 190], "branches": []}
# gained: {"lines": [189, 190], "branches": []}

import pytest

# Assuming the InvalidSource class is defined in a module named apt_repository
from ansible.modules.apt_repository import InvalidSource

def test_invalid_source_exception():
    with pytest.raises(InvalidSource):
        raise InvalidSource("This is an invalid source")

# No cleanup is necessary for this test as it only raises and catches an exception
