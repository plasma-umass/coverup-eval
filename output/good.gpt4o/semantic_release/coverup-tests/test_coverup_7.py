# file semantic_release/hvcs.py:345-347
# lines [345, 346]
# branches []

import pytest
from semantic_release.hvcs import Base

def test_gitlab_class():
    class Gitlab(Base):
        """Gitlab helper class"""
    
    # Create an instance of the Gitlab class
    gitlab_instance = Gitlab()
    
    # Assert that the instance is indeed an instance of Gitlab
    assert isinstance(gitlab_instance, Gitlab)
    
    # Assert that the instance is also an instance of Base
    assert isinstance(gitlab_instance, Base)
