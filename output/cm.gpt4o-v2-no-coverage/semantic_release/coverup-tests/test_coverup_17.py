# file: semantic_release/hvcs.py:23-49
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49], "branches": []}

import pytest
from semantic_release.hvcs import Base

def test_domain_not_implemented():
    with pytest.raises(NotImplementedError):
        Base.domain()

def test_api_url_not_implemented():
    with pytest.raises(NotImplementedError):
        Base.api_url()

def test_token_not_implemented():
    with pytest.raises(NotImplementedError):
        Base.token()

def test_check_build_status_not_implemented():
    with pytest.raises(NotImplementedError):
        Base.check_build_status("owner", "repo", "ref")

def test_post_release_changelog_not_implemented():
    with pytest.raises(NotImplementedError):
        Base.post_release_changelog("owner", "repo", "version", "changelog")

def test_upload_dists():
    assert Base.upload_dists("owner", "repo", "version", "path") == True
