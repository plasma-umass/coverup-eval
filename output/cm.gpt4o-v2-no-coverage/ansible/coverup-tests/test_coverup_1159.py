# file: lib/ansible/modules/apt_repository.py:516-524
# asked: {"lines": [520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 520], [521, 522]]}
# gained: {"lines": [520, 521, 522, 524], "branches": [[520, 521], [520, 524], [521, 522]]}

import os
import pytest
from unittest.mock import MagicMock
from ansible.modules.apt_repository import revert_sources_list

def test_revert_sources_list(monkeypatch):
    # Mock the os.path.exists and os.remove functions
    mock_exists = MagicMock(side_effect=lambda x: x in ["new_file"])
    mock_remove = MagicMock()
    monkeypatch.setattr(os.path, "exists", mock_exists)
    monkeypatch.setattr(os, "remove", mock_remove)

    # Mock sources_before and sources_after
    sources_before = {"existing_file": "content"}
    sources_after = {"existing_file": "content", "new_file": "new_content"}

    # Mock sourceslist_before
    sourceslist_before = MagicMock()

    # Call the function
    revert_sources_list(sources_before, sources_after, sourceslist_before)

    # Assertions
    mock_exists.assert_called_once_with("new_file")
    mock_remove.assert_called_once_with("new_file")
    sourceslist_before.save.assert_called_once()

    # Clean up
    mock_exists.reset_mock()
    mock_remove.reset_mock()
    sourceslist_before.save.reset_mock()
