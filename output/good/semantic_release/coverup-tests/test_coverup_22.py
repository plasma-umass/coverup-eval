# file semantic_release/hvcs.py:502-508
# lines [502, 508]
# branches []

import pytest
from unittest.mock import MagicMock
from semantic_release.hvcs import check_token

@pytest.fixture
def mock_hvcs(mocker):
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=MagicMock(token=MagicMock(return_value=None)))

def test_check_token_with_no_token(mock_hvcs):
    assert not check_token(), "check_token should return False when there is no token"
