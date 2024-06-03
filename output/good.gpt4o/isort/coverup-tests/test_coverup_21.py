# file isort/exceptions.py:74-82
# lines [74, 75, 77, 78, 79, 80, 82]
# branches []

import pytest
from isort.exceptions import ProfileDoesNotExist, ISortError

def test_profile_does_not_exist(mocker):
    profile_name = "non_existent_profile"
    available_profiles = ["default", "black", "google"]
    
    mocker.patch('isort.exceptions.profiles', available_profiles)
    
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile_name)
    
    assert str(exc_info.value) == (
        f"Specified profile of {profile_name} does not exist. "
        f"Available profiles: {','.join(available_profiles)}."
    )
    assert exc_info.value.profile == profile_name
    assert isinstance(exc_info.value, ISortError)
