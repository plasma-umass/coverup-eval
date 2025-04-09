# file mimesis/providers/path.py:36-39
# lines [36, 37, 39]
# branches []

import pytest
from mimesis.providers.path import Path

def test_path_meta_name():
    # Create an instance of the Path provider
    path_provider = Path()
    
    # Assert that the Meta class name attribute is 'path'
    assert path_provider.Meta.name == 'path'
