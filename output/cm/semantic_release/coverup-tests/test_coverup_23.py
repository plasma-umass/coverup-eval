# file semantic_release/dist.py:31-34
# lines [31, 32, 33, 34]
# branches []

import os
import pytest
from unittest.mock import patch
from semantic_release import dist

# Assuming the logger is imported in the dist module as follows:
# from semantic_release import logger

@pytest.fixture
def temp_dist_dir(tmp_path):
    dist_dir = tmp_path / "dists"
    dist_dir.mkdir()
    (dist_dir / "dummy_file").write_text("dummy content")
    return str(dist_dir)

def test_remove_dists(temp_dist_dir, mocker):
    mock_run = mocker.patch('semantic_release.dist.run')
    mock_logger = mocker.patch('semantic_release.dist.logger')
    dist.remove_dists(temp_dist_dir)
    mock_logger.debug.assert_called_once()
    mock_run.assert_called_once_with(f"rm -rf {temp_dist_dir}")
