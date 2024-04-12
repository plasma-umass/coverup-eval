# file thonny/jedi_utils.py:134-135
# lines [134, 135]
# branches []

import pytest
from thonny.jedi_utils import _using_older_jedi
from unittest.mock import MagicMock

@pytest.fixture
def mock_jedi_version():
    mock_jedi = MagicMock()
    yield mock_jedi
    del mock_jedi

@pytest.mark.parametrize("version, expected_result", [
    ("0.13.0", True),
    ("0.14.1", True),
    ("0.15.2", True),
    ("0.16.0", True),
    ("0.17.0", True),
    ("0.18.0", False),
    ("1.0.0", False),
    ("2.0.0", False),
])
def test_using_older_jedi(mock_jedi_version, version, expected_result):
    mock_jedi_version.__version__ = version
    assert _using_older_jedi(mock_jedi_version) == expected_result
