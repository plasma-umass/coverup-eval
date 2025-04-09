# file: isort/exceptions.py:74-82
# asked: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}
# gained: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}

import pytest
from isort.exceptions import ProfileDoesNotExist
from isort.profiles import profiles

def test_profile_does_not_exist():
    profile_name = "non_existent_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile_name)
    
    exception_message = str(exc_info.value)
    assert profile_name in exception_message
    assert "Available profiles:" in exception_message
    for profile in profiles:
        assert profile in exception_message
    assert exc_info.value.profile == profile_name
