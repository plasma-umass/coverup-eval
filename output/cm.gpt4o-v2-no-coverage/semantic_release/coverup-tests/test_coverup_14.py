# file: semantic_release/hvcs.py:442-452
# asked: {"lines": [442, 451, 452], "branches": []}
# gained: {"lines": [442, 451, 452], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import check_build_status, get_hvcs, Base
from semantic_release.errors import ImproperConfigurationError

class MockHVCS(Base):
    @staticmethod
    def check_build_status(owner: str, repo: str, ref: str) -> bool:
        return True

@pytest.fixture
def mock_hvcs(monkeypatch):
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: MockHVCS)

def test_check_build_status_success(mock_hvcs):
    assert check_build_status("owner", "repo", "ref") is True

def test_check_build_status_improper_configuration(monkeypatch):
    monkeypatch.setattr('semantic_release.hvcs.config', {'hvcs': 'invalid'})
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
