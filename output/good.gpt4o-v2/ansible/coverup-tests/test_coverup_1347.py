# file: lib/ansible/module_utils/api.py:69-93
# asked: {"lines": [71, 72, 73, 75, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93], "branches": [[72, 73], [72, 75], [79, 80], [79, 82], [83, 84], [83, 89], [86, 87], [86, 88]]}
# gained: {"lines": [71, 72, 73, 75, 76, 78, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93], "branches": [[72, 73], [72, 75], [79, 80], [83, 84], [83, 89], [86, 87]]}

import pytest
import sys
import time
from unittest.mock import patch

from ansible.module_utils.api import rate_limit as rate_limit_decorator

@pytest.mark.parametrize("rate, rate_limit, expected_minrate", [
    (10, 100, 10.0),
    (5, 20, 4.0),
    (None, 100, None),
    (10, None, None),
    (None, None, None),
])
def test_rate_limit(rate, rate_limit, expected_minrate):
    decorator = rate_limit_decorator(rate, rate_limit)
    assert decorator is not None

    @decorator
    def dummy_function():
        return "test"

    with patch('time.sleep', return_value=None) as mock_sleep:
        if expected_minrate is not None:
            start_time = time.process_time() if sys.version_info >= (3, 8) else time.clock()
            result = dummy_function()
            end_time = time.process_time() if sys.version_info >= (3, 8) else time.clock()
            elapsed = end_time - start_time
            assert result == "test"
            assert elapsed >= 0  # Ensure elapsed time is non-negative
            mock_sleep.assert_called_once()
        else:
            result = dummy_function()
            assert result == "test"
            mock_sleep.assert_not_called()
