# file: lib/ansible/modules/apt_repository.py:189-190
# asked: {"lines": [189, 190], "branches": []}
# gained: {"lines": [189, 190], "branches": []}

import pytest
from ansible.modules.apt_repository import InvalidSource

def test_invalid_source_exception():
    with pytest.raises(InvalidSource):
        raise InvalidSource("This is a test exception")

def test_invalid_source_message():
    try:
        raise InvalidSource("This is a test exception")
    except InvalidSource as e:
        assert str(e) == "This is a test exception"
