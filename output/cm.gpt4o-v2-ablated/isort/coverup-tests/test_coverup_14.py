# file: isort/exceptions.py:74-82
# asked: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}
# gained: {"lines": [74, 75, 77, 78, 79, 80, 82], "branches": []}

import pytest
from isort.exceptions import ProfileDoesNotExist, ISortError

def test_profile_does_not_exist(monkeypatch):
    # Mock the profiles list to ensure consistent test results
    mock_profiles = ["black", "google", "yapf"]
    monkeypatch.setattr("isort.exceptions.profiles", mock_profiles)

    profile_name = "nonexistent_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile_name)
    
    assert str(exc_info.value) == (
        f"Specified profile of {profile_name} does not exist. "
        f"Available profiles: {','.join(mock_profiles)}."
    )
    assert exc_info.value.profile == profile_name
    assert isinstance(exc_info.value, ISortError)
