# file semantic_release/hvcs.py:23-49
# lines [26, 30, 34, 38, 44]
# branches []

import pytest
from semantic_release.hvcs import Base

def test_base_methods_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Base.domain()
    with pytest.raises(NotImplementedError):
        Base.api_url()
    with pytest.raises(NotImplementedError):
        Base.token()
    with pytest.raises(NotImplementedError):
        Base.check_build_status('owner', 'repo', 'ref')
    with pytest.raises(NotImplementedError):
        Base.post_release_changelog('owner', 'repo', 'version', 'changelog')
