# file semantic_release/hvcs.py:23-49
# lines [23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49]
# branches []

import pytest
from semantic_release.hvcs import Base

class MockHVCS(Base):
    @staticmethod
    def domain() -> str:
        return "mock.domain"

    @staticmethod
    def api_url() -> str:
        return "https://api.mock.domain"

    @staticmethod
    def token() -> str:
        return "mocktoken"

    @staticmethod
    def check_build_status(owner: str, repo: str, ref: str) -> bool:
        return True

    @classmethod
    def post_release_changelog(
        cls, owner: str, repo: str, version: str, changelog: str
    ) -> bool:
        return True

def test_upload_dists():
    owner = "mock_owner"
    repo = "mock_repo"
    version = "1.0.0"
    path = "/path/to/dists"

    result = MockHVCS.upload_dists(owner, repo, version, path)
    assert result is True
