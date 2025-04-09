# file semantic_release/hvcs.py:23-49
# lines [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49]
# branches []

import pytest
from semantic_release.hvcs import Base

def test_base_class_methods():
    # Test that NotImplementedError is raised for the methods that should raise it
    with pytest.raises(NotImplementedError):
        Base.domain()
    
    with pytest.raises(NotImplementedError):
        Base.api_url()
    
    with pytest.raises(NotImplementedError):
        Base.token()
    
    with pytest.raises(NotImplementedError):
        Base.check_build_status("owner", "repo", "ref")
    
    with pytest.raises(NotImplementedError):
        Base.post_release_changelog("owner", "repo", "version", "changelog")
    
    # Test that upload_dists returns True
    assert Base.upload_dists("owner", "repo", "version", "path") == True
