# file flutils/pathutils.py:504-560
# lines [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560]
# branches ['553->554', '553->555']

import os
import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

@pytest.fixture
def mock_environment(tmp_path, monkeypatch):
    # Set up a temporary directory and environment variables
    monkeypatch.setenv('TEST_VAR', 'test_value')
    monkeypatch.setattr(os, 'getcwd', lambda: str(tmp_path))
    # Create a non-absolute path that includes an environment variable and a tilde
    non_abs_path = '~/somepath/$TEST_VAR/../anotherpath'
    # Yield the non-absolute path for testing
    yield non_abs_path
    # No cleanup needed as pytest handles the temporary directory

def test_normalize_path_non_absolute(mock_environment):
    # Use the non-absolute path from the fixture
    non_abs_path = mock_environment
    # Normalize the path
    normalized = normalize_path(non_abs_path)
    # Assert that the normalized path is absolute and correct
    assert normalized.is_absolute()
    home_dir = Path.home()
    expected_path = home_dir / 'somepath' / 'test_value' / '..' / 'anotherpath'
    expected_path = expected_path.resolve()
    assert normalized == expected_path
