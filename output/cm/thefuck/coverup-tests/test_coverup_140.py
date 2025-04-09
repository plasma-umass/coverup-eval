# file thefuck/conf.py:115-127
# lines [118]
# branches ['117->118']

import pytest
from thefuck.conf import Settings

@pytest.fixture
def mock_args(mocker):
    return mocker.Mock(yes=False, debug=False, repeat=False)

def test_settings_from_args_empty():
    settings = Settings()
    result = settings._settings_from_args(None)
    assert result == {}
