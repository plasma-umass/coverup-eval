# file: semantic_release/hvcs.py:52-64
# asked: {"lines": [52, 64], "branches": []}
# gained: {"lines": [52, 64], "branches": []}

import pytest
import mimetypes
from semantic_release.hvcs import _fix_mime_types

def test_fix_mime_types(monkeypatch):
    # Backup the original types
    original_types = mimetypes.types_map.copy()

    # Ensure the .md type is not set initially
    if '.md' in mimetypes.types_map:
        del mimetypes.types_map['.md']

    # Run the function to fix mime types
    _fix_mime_types()

    # Assert that the .md type is now set correctly
    assert mimetypes.types_map['.md'] == 'text/markdown'

    # Restore the original types to avoid state pollution
    mimetypes.types_map.clear()
    mimetypes.types_map.update(original_types)
