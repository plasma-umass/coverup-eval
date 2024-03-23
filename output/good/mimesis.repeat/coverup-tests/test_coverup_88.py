# file mimesis/providers/path.py:36-39
# lines [36, 37, 39]
# branches []

import pytest
from mimesis.providers.path import Path

def test_path_meta():
    path_provider = Path()
    assert path_provider.Meta.name == 'path'
