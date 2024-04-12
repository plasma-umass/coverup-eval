# file flutes/timing.py:9-34
# lines [9, 10, 30, 31, 32, 33, 34]
# branches []

import pytest
from unittest.mock import patch
from flutes.timing import work_in_progress
import time

def test_work_in_progress():
    with patch("flutes.timing.print") as mock_print:
        with patch("flutes.timing.time.time", side_effect=[0, 2]):
            with work_in_progress("Testing"):
                time.sleep(1)
            mock_print.assert_any_call("Testing... ", end='', flush=True)
            mock_print.assert_any_call("done. (2.00s)")

def test_work_in_progress_decorator():
    with patch("flutes.timing.print") as mock_print:
        with patch("flutes.timing.time.time", side_effect=[0, 3]):
            @work_in_progress("Decorated function")
            def dummy_function():
                time.sleep(1)
            dummy_function()
            mock_print.assert_any_call("Decorated function... ", end='', flush=True)
            mock_print.assert_any_call("done. (3.00s)")
