# file: isort/exceptions.py:74-82
# asked: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}
# gained: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}

import pytest
from isort.exceptions import ProfileDoesNotExist
from isort.profiles import profiles

def test_profile_does_not_exist():
    non_existent_profile = "non_existent_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(non_existent_profile)
    
    assert str(exc_info.value) == (
        f"Specified profile of {non_existent_profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert exc_info.value.profile == non_existent_profile
