# file isort/exceptions.py:74-82
# lines [74, 75, 77, 78, 79, 80, 82]
# branches []

import pytest
from isort.exceptions import ProfileDoesNotExist

def test_profile_does_not_exist_exception():
    profile_name = "non_existent_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile_name)
    
    exception = exc_info.value
    assert profile_name == exception.profile
    assert "Specified profile of non_existent_profile does not exist." in str(exception)
