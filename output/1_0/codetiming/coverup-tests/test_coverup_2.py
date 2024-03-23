# file codetiming/_timer.py:72-74
# lines [72, 74]
# branches []

import pytest
from codetiming import Timer
from unittest.mock import patch

def test_timer_context_manager():
    with patch.object(Timer, 'stop') as mock_stop:
        with Timer():
            pass
        mock_stop.assert_called_once()

def test_timer_context_manager_with_exception():
    with patch.object(Timer, 'stop') as mock_stop:
        with pytest.raises(ZeroDivisionError):
            with Timer():
                1 / 0  # This will raise a ZeroDivisionError
        mock_stop.assert_called_once()
