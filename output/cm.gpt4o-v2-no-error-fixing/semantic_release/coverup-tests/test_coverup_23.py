# file: semantic_release/hvcs.py:23-49
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49], "branches": []}

import pytest
from semantic_release.hvcs import Base

def test_base_domain():
    with pytest.raises(NotImplementedError):
        Base.domain()

def test_base_api_url():
    with pytest.raises(NotImplementedError):
        Base.api_url()

def test_base_token():
    with pytest.raises(NotImplementedError):
        Base.token()

def test_base_check_build_status():
    with pytest.raises(NotImplementedError):
        Base.check_build_status("owner", "repo", "ref")

def test_base_post_release_changelog():
    with pytest.raises(NotImplementedError):
        Base.post_release_changelog("owner", "repo", "version", "changelog")

def test_base_upload_dists():
    assert Base.upload_dists("owner", "repo", "version", "path") == True
